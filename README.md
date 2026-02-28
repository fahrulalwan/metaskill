# metaskill

Teach your AI agent how to actually learn — not just log.

## The Problem

Most agents log mistakes. They don't learn from them.

After auditing my OpenClaw agent's learning system:
- 37 corrections logged. All surface-level. "Don't use tool X." Nothing deeper.
- Same mistake logged 3 times. Still happened a fourth.
- Win:error ratio — 0:24. Only learned from failure, never success.
- Cross-domain transfer: basically zero.

**It wasn't learning. It was archiving.**

## What metaskill Does

Three scripts. One monthly eval.

| Script | What it does |
|---|---|
| `deep-correct.sh` | Forces 3-level breakdown per error: surface → principle → habit |
| `transfer-check.sh` | Scans past patterns before non-trivial tasks |
| `success-capture.sh` | Logs what worked, not just what broke |
| `eval.sh` | Monthly score to track if you're actually improving |

## Install

```bash
clawhub install metaskill
```

Requires [OpenClaw](https://openclaw.ai). Zero other dependencies.

## Version

- **v1.0** — keyword-based, intentional. A rough habit beats a perfect system you never run.
- **v1.1** *(coming)* — LLM-powered extraction, semantic transfer check.

## License

MIT
