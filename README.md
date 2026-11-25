# Nova Copilot MVP

A demo support copilot for Nova Bank that runs on synthetic data. It answers questions about disputes, fees and card replacement from policy sections and the signed-in customer's own transactions. Every answer is checked by guardrails, and the app also has an eval suite, an agent queue and an audit log.

Everything is in a single file: `index.html`.

## Run locally

```
python -m http.server 5173
```

Then open http://localhost:5173.

When the page runs outside claude.ai, the AI model isn't available, so the header shows "AI: off" and every answer comes from the built-in rule-based pipeline. The guardrails and the evals still work.
