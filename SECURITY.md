# Security

## ClawHub Scanner Notice

This skill reads `ANTHROPIC_API_KEY` and `OPENAI_API_KEY` from **environment variables only** — never from files, never transmitted externally.

These keys are **optional** and only used for v1.1 LLM-powered extraction (not yet released). v1.0 is fully offline/local.

**What the scripts do:**
- Read/write to your local `memory/` directory (workspace only)
- No network requests in v1.0
- No data leaves your machine

You can verify this by reviewing:
- `scripts/deep-correct.sh` — pure bash, local file writes only
- `scripts/transfer-check.sh` — pure bash, local grep only
- `scripts/success-capture.sh` — pure bash, local file writes only
- `scripts/eval.sh` — pure bash, local file reads only
- `scripts/llm_extract.py` — optional, only runs if API key is set

## Reporting Vulnerabilities

Open an issue or email fahrulalwan@gmail.com.
