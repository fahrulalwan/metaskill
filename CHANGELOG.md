# Metaskill Changelog

## v1.3.0 — 2026-03-01

### feat: Abstract provider system

- Added `config.yaml` — configure fast/deep provider tiers without touching code
- Added `llm_provider.py` — unified wrapper supporting anthropic, openai, ollama, gemini
- Refactored `llm_extract.py` + `llm_transfer.py` to use `llm_provider.call_llm()`
- Updated `eval.sh` — reads provider config instead of hardcoded env var checks
- Updated `SKILL.md` — added Configuration section with provider table + Ollama example
- **Breaking:** No longer hardcodes `ANTHROPIC_API_KEY` / `OPENAI_API_KEY` directly. Edit `config.yaml` to set your provider.

## v1.2.0 — prior

- LLM-powered extraction with Anthropic/OpenAI fallback
- eval.sh scoring system
- transfer-check.sh for analogical learning

## v1.1.0 — prior

- deep-correct.sh 3-level breakdown
- success-capture.sh pattern logging

## v1.0.0 — initial

- Core metaskill framework
