# Changelog

## v1.1.0 (2026-02-28)

### Added
- LLM-powered extraction for deeper error analysis with graceful offline fallback.
- Semantic transfer check using LLM to find analogous principles beyond simple keyword matching.
- Explicit UI modes: "[LLM mode]" and "[offline mode]" indicators.

## v1.0.0 (2026-02-28)

### Added
- `deep-correct.sh` — 3-level error breakdown (surface → principle → habit)
- `transfer-check.sh` — pre-task pattern check from past learnings
- `success-capture.sh` — log what worked, not just what broke
- `eval.sh` — monthly learning score with trend tracking
- `llm_extract.py` / `llm_transfer.py` — base scripts for LLM integration.
