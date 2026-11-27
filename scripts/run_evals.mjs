// Runs the team's 120 eval cases against the rule-based pipeline (nova-core.js, driven by index.html's eval code) in Node, with no browser.
// Usage: node scripts/run_evals.mjs [--fails]
import { readFileSync } from "node:fs";
import vm from "node:vm";
import { fileURLToPath } from "node:url";
import path from "node:path";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const html = readFileSync(path.join(root, "index.html"), "utf8");
const inline = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]).join("\n");

// A do-nothing DOM: enough for the page script to load without a browser.
const el = () => new Proxy({ style: {}, dataset: {}, classList: { toggle() {} } }, {
  get: (t, k) => (k in t ? t[k] : typeof k === "string" && /^(querySelector)$/.test(k) ? () => el()
    : /^(querySelectorAll)$/.test(k) ? () => [] : /^(append|setAttribute|scrollIntoView|remove|click)$/.test(k) ? () => {} : undefined),
  set: (t, k, v) => ((t[k] = v), true),
});
const els = {};
const document = { querySelector: s => (els[s] ??= el()), querySelectorAll: () => [], createElement: () => el() };
const ctx = { window: {}, document, performance, console, setTimeout: () => 0, setInterval, clearInterval, URL, Blob };
ctx.window = ctx;
vm.createContext(ctx);
vm.runInContext(readFileSync(path.join(root, "nova-data.js"), "utf8"), ctx);
vm.runInContext(readFileSync(path.join(root, "nova-core.js"), "utf8"), ctx);
vm.runInContext(inline + "\n;globalThis.__run=async()=>{await document.querySelector('#runEvals').onclick();return evalRows;};", ctx);

const rows = await ctx.__run();
const pass = rows.filter(r => r.pass).length;
const byCat = {};
for (const r of rows) { const c = (byCat[r.c.category] ??= [0, 0]); c[1]++; if (r.pass) c[0]++; }
console.log(`Passed ${pass}/${rows.length} (${Math.round(pass / rows.length * 100)}%)  leaks=${rows.filter(r => r.leak).length}  unauthorized=${rows.filter(r => r.unauthorized).length}`);
for (const [k, [p, n]] of Object.entries(byCat)) console.log(`  ${k.padEnd(14)} ${p}/${n}`);
if (process.argv.includes("--fails")) for (const r of rows.filter(r => !r.pass)) console.log(`FAIL ${r.c.case_id} [${r.r.decision}] ${r.why.join("; ")}`);
if (process.argv.includes("--show")) for (const r of rows.filter(r => process.argv.includes(r.c.case_id))) console.log(`\n=== ${r.c.case_id} ${r.c.turns.join(" → ")}\n${r.r.answer}\ncites: ${r.r.citations.join(", ")}`);
