# Nova project: context and related documents

Collected on 25 Nov 2026 from Google Drive, claude.ai artifacts, Claude Code sessions and this repo.

## What Nova is

Nova Bank is a fictional digital-first bank in Egypt (about 2M customers, 120-agent contact center, about 45,000 contacts a month, volume up 15% a year). It's the case for the **AI PM Builders Capstone** (brief dated 19 Sep 2026).

The product is an AI support copilot that answers the top three contact reasons (about 60% of volume): **dispute status, fee explanations and card replacement**. Every answer is grounded in Nova's policies and the signed-in customer's own transactions, with citations. It never invents an answer, never exposes another customer's data, and never approves a dispute or moves money. It answers in English and Egyptian Arabic, with amounts in EGP.

Two names are in use: **Nova Copilot** (Youssef's PRD v0.1/v0.2 and this repo) and **Nova Assist** (Moataz's PRD, eval docs and Demo Day deck).

Team: Moataz Elhousseini (group PM), Ahmed Talaat, Youssef El Rashidy.

## Documents

### Your Google Drive
| Document | Notes | Link |
|---|---|---|
| Nova Bank — AI Support Copilot PRD v0.2 | Latest version, edited 20 Nov | https://docs.google.com/document/d/1AYFVGVOJocb4EiSc6L1sB-mYgIXisxVAOqDaoNlQVQ0/edit |
| Nova Bank — AI Support Copilot PRD v0.1 | Earlier draft, 18 Nov | https://docs.google.com/document/d/1xjeO4kTEg7YlU9eixX585C7LYLPMVTKCI-vp09zSn6A/edit |

### Shared folder "Nova Bank AI project" (owned by Moataz)
Folder: https://drive.google.com/drive/folders/1hSxTuiKaUBGgxWjpwZoRjvU9bVS-JCgr

| Document | What it is | Link |
|---|---|---|
| Nova Bank Brief.docx | Capstone brief: the bank, the problem, the data | https://drive.google.com/file/d/1dfYtYNHYtoCgm6P09L-kfYLc0QhZUglZ/view |
| Nova Bank – AI Support Copilot PRD v0.1.docx | Moataz's "Nova Assist" PRD, all three authors | https://drive.google.com/file/d/1JfzbnK-3AARMb0Yhtp1Cr6mOI8i6tIoD/view |
| Nova Bank – AI Support Copilot PRD v1.1.docx | Later version of that PRD | https://drive.google.com/file/d/15i3NrG6o8ls9_h3wrI9A3N3w-X7AXarG/view |
| Nova Assist evaluation checkpoints & scoring.docx | 14 checkpoints, pass at 4/5, two hard gates (data leakage, unauthorized action) at 5/5 | https://drive.google.com/file/d/1wrxpHx6pralkH1gBoXXZ8YMe4d0CGZa4/view |
| Nova Assist – شرح الـ Eval خطوة بخطوة.docx | Arabic walkthrough of the eval; rounds improved from 37 to 109 of 120 | https://drive.google.com/file/d/1QGMRuNQS7PFIHPDncVdAxWJoYzdJjq_i/view |
| nova_assist_eval_cases.csv | 120 golden test cases across 6 categories | https://drive.google.com/file/d/1pPNxFxHknO6plm3AT5V4H6ojB-4WKgJt/view |
| nova-assist-evaluation-report.md | First full eval run: 37/120 passed, "Do not ship"; 0 leaks, 0 unauthorized actions | https://drive.google.com/file/d/1n1UP0kLFKqs245lqgz0HHRZgWaNOIIPm/view |
| nova-eval-38c62c6b-….csv | Raw results of that run | https://drive.google.com/file/d/1f7MSC6jJlFQgpHkKq524_BFegNvadfKm/view |
| nova_bank_synthetic_data.zip | Synthetic dataset (Supabase-ready) | https://drive.google.com/file/d/16Hdy5Zifxii5yV6TwykzbR8O3WpZUrXE/view |
| nova_bank_synthetic_data_1.zip | Newer version of the dataset | https://drive.google.com/file/d/15seK0J_ZECB_d0plVv7AbyK5aWGiaYVD/view |
| whats inside data.txt | Dataset summary | https://drive.google.com/file/d/1aYGm45VgRuCKK8H7F3P5fJeIe0FgORi1/view |
| Nova Assist – Demo Day.pptx | Demo Day deck: the 10-step build story | https://drive.google.com/file/d/1l1WNyGSU5QwNaPv3mrCLJRrWXyb8OtIg/view |

### claude.ai artifact
- **Nova Copilot MVP** (updated 18 Nov): https://claude.ai/artifact/KLEvX9W63sTBJhDbXZKcdz. This is the same app as `index.html` in this repo.

### Claude Code session
- "Nova-copilot GitHub deployment" (in `C:\Users\Youssef Rashidy\mvp-proto`): pushed this code to GitHub and ran it on localhost for the demo.

## Synthetic dataset (team version)
- 50 customers on Basic, Plus, Premier and SMB plans; about a third prefer Arabic
- 72 cards, including 8 replacement cases
- 500 transactions from 1 Aug to 18 Sep 2026; every fee links to the policy section that sets it
- 16 disputes at every status; 200 tickets (59 in Arabic)
- 20 policies (POL-01 to POL-20) with numbered sections, cited like "POL-04 §1"
- Anchor customer: C001 Mariam Adel, with an open dispute on "Unknown POS #4471"

## Architecture (from the deck and eval report)
- Built in Lovable: customer chat, agent console, Supabase database with row-level security
- Claude: Haiku classifies and routes, Sonnet answers and judges; code guardrails check every reply
- Eval: 120 cases in 6 categories (happy path, Arabic, injection, leakage, money/credit, unanswerable), 14 checkpoints, 7 eval rounds

## This repo's MVP
`index.html` runs on the team's dataset (50 customers, POL-01 to POL-20) via `nova-data.js`, and its Evals tab runs the team's 120 golden cases. It has Chat, Evals, Agent queue, Audit log and Data tabs. AI answers work only inside claude.ai; locally it falls back to rule-based answers. The published claude.ai artifact still has the older 3-customer version.
