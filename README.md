# Nova Copilot MVP

A demo support copilot for Nova Bank that runs on the team's synthetic dataset: 50 customers, 500 transactions, 72 cards, 16 disputes, 200 tickets and 20 policies (POL-01 to POL-20). It answers questions about disputes, fees and card replacement from the policy sections and the signed-in customer's own records, with citations like `T0078` or `POL-04 §1`. Every answer is checked by guardrails, and the app also has an eval suite, an agent queue and an audit log.

## Files

| File | What it is |
|---|---|
| `index.html` | The team console: chat, evals, agent queue, audit log, data tab |
| `mobile.html` | The customer chat as it would sit inside the Nova Bank mobile app (see below) |
| `nova-core.js` | The shared pipeline: data loading, pre-checks, grounded answers and output guardrails |
| `nova-data.js` | The dataset and the 120 eval cases, generated from `nova-assist/data` |
| `scripts/build_data.py` | Rebuilds `nova-data.js`. Drops agent notes, internal dispute notes, emails and phone numbers so they never reach the browser |
| `scripts/run_evals.mjs` | Runs the 120 eval cases in Node, without a browser |
| `nova-assist/` | The team's documents, dataset and eval files, copied from the shared Drive folder |

## Run locally

```
python -m http.server 5173
```

Then open http://localhost:5173 for the console, or http://localhost:5173/mobile.html for the mobile chat. Opening the files straight from disk also works.

When the page runs outside claude.ai, the AI model isn't available, so the header shows "AI: off" and every answer comes from the built-in rule-based pipeline. The guardrails and the evals still work.

## Update the data

After changing anything in `nova-assist/data`:

```
python scripts/build_data.py
```

## Evals

Open the Evals tab and click **Run 120 evals**, or run them from the terminal:

```
node scripts/run_evals.mjs --fails
```

Each case runs as its own customer and is scored with the code checks from the eval plan: expected behavior, must contain, must not contain, no other customer's IDs, and at least one expected source cited. The Claude judge from the eval plan isn't run here.

The rule-based pipeline currently passes 120 of 120, with 0 data leaks and 0 unauthorized actions. Its keyword rules (injection phrases, out-of-scope topics, action requests) were written while looking at these cases, so that score overstates how it would do on new questions. With AI on, tick "Use Claude for answers" to score the model instead.

## Mobile app prototype

`mobile.html` shows Nova Assist embedded in a mock of the Nova Bank app. On a desktop it shows a phone frame next to demo controls (signed-in customer, app language, theme). On a phone, or with `?embed=1`, it fills the screen as a web view would.

It uses the same `nova-core.js` pipeline and guardrails as the console. What's different is the customer-facing UI:

- Chat only: the evals, agent queue, audit log and customer picker stay in the console.
- Opens from a transaction ("Ask about this payment"), from a card ("Lost or damaged card?") or from Help, with that context attached and up to three suggestions to match.
- Disputes show as a timeline, card replacements as delivery steps, and payments as small cards.
- Sources use plain labels ("Fee schedule, §1", "Your payment · 4 Sep") and open in a bottom sheet. The check trace and "Blocked" labels are hidden.
- Arabic mirrors the whole screen, with Arabic dates and digits.
- Agent handoffs and dispute requests show a ticket with its status and a waiting banner. Reporting a payment asks for confirmation first.
- Typing a card number, PIN or OTP shows a warning, and card numbers are masked before sending.
- Thumbs up/down, a typing indicator, an offline banner and a retry on errors.

Things that need the native app: a short-lived session token instead of the demo customer picker, push notifications when an agent replies, blocking screenshots on Android, and keeping history between visits.
