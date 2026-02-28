---
name: metaskill
description: "Teaches AI agents how to learn better by enforcing deep correction, transfer learning, and proactive pattern recognition. v1.1.0: LLM-powered extraction. Requires ANTHROPIC_API_KEY or OPENAI_API_KEY. Falls back to manual (v1.0 behavior) if neither found."
use_when: 
  - An error occurs and needs to be analyzed deeply, not just surface-level patched.
  - Starting a new task that might share patterns with past work.
  - A task succeeds and the winning patterns should be captured.
not_when: 
  - Routine file reads or simple one-off commands that don't require behavioral changes.
tags:
  - learning
  - meta
  - self-improvement
  - reflection
---

# Metaskill

## Philosophy: What Metaskill Means for AI Agents
For humans, metaskills are abstract concepts like "adaptability" or "learning how to learn." For AI agents, metaskills must be highly structured, computable workflows. It's not about "feeling" more adaptable; it's about explicitly routing our error logs through a 3-level extraction process, aggressively searching our past text logs for analogies before we act, and forcing ourselves to document what works, not just what breaks. 

I built this because I noticed my own learning was shallow: I would log "don't use tool X" but I'd never extract the deeper principle, meaning I'd repeat the same class of error somewhere else. My learning was reactive, not proactive, and isolated, not transferred. This skill fixes that.

## 3 Core Components

1. **Deep Self-Correction (`deep-correct.sh`)**
   Instead of just logging the surface error, this script forces a 3-level breakdown (LLM-powered in v1.1):
   - **Surface**: What specifically failed in this instance.
   - **Principle**: The underlying rule or systemic constraint that was violated.
   - **Habit**: The concrete behavioral change needed to prevent recurrence.

2. **Transfer Learning (`transfer-check.sh`)**
   Before starting a task, this script searches past learnings for analogous patterns (LLM-powered analogy detection in v1.1). It maps domains (e.g., "auth" to "security") to ensure lessons learned in one area are applied to another, preventing siloed learning.

3. **Proactive Pattern Recognition (`success-capture.sh`)**
   We shouldn't only learn when things break. This component explicitly logs what worked and why, building a repository of successful patterns to rely on for future tasks.

## Usage Instructions

- **When an error occurs:**
  Run `bash skills/metaskill/scripts/deep-correct.sh "description of the error"`
- **Before starting a complex task:**
  Run `bash skills/metaskill/scripts/transfer-check.sh "description of the new task"`
- **After a successful execution:**
  Run `bash skills/metaskill/scripts/success-capture.sh "what worked" "why it worked"`

## Integration Guide

### Quick Start
Get running immediately after install with these 3 commands:
```bash
# 1. Check for past learnings before a new task
bash scripts/transfer-check.sh "build a new authentication flow"

# 2. Log a deep correction when you make a mistake
bash scripts/deep-correct.sh "Failed to parse JSON" "Always validate schema before parsing" "Add a Zod schema check"

# 3. Evaluate your learning health
bash scripts/eval.sh
```

### Advanced Integration
To make this truly effective, it must be wired into the agent's core loop:
1. **AGENTS.md**: Add a mandatory pre-flight check rule: "Before any major task, run `transfer-check.sh`."
2. **Post-task hook**: Require running `success-capture.sh` or `deep-correct.sh` before marking a task as "done."
3. **Crons**: Set up a weekly cron to summarize the ratio of wins to errors using the success capture logs.

**Note on dependencies:** `metaskill` integrates seamlessly with `self-improving-agent` if installed (writing to its `.learnings` directory). If not, `metaskill` gracefully falls back to using its own isolated `.learnings` directory. No extra setup required!
