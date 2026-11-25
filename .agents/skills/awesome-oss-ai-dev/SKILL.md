---
name: awesome-oss-ai-dev
description: "Pick proven open-source AI building blocks for software work: LLM frameworks, inference engines, agent/multi-agent systems, RAG, eval harnesses, MLOps, UIs. Consults a local clone of awesome-opensource-ai (14 curated sections). Use when choosing a model, library, inference server, agent framework, RAG stack, eval tool, or self-hosted AI platform — or when the user asks what open-source options exist."
---

# Awesome Open-Source AI — Dev Selection Guide

Local clone of [alvinreal/awesome-opensource-ai](https://github.com/alvinreal/awesome-opensource-ai)
(daily-updated upstream): `~/Projects/awesome-opensource-ai/README.md` (~1500 lines, 14 sections).

## When to use

- User needs an open-source model, framework, inference engine, agent framework,
  RAG library, eval harness, vector DB, or self-hosted UI — check here FIRST
  before recommending from memory (memory goes stale; this list is updated daily).
- Comparing options in a category (e.g. inference: vLLM vs TensorRT-LLM vs llama.cpp).
- Scaffolding agentic work: start from section 4 (Agentic AI) + section 5 (RAG).

## How to use

```bash
# Refresh the list (upstream updates daily)
git -C ~/Projects/awesome-opensource-ai pull --ff-only

# Find candidates in a section (sections are numbered 1-14, see map below)
grep -n -i "inference" ~/Projects/awesome-opensource-ai/README.md | head -20
sed -n '<start>,<end>p' ~/Projects/awesome-opensource-ai/README.md
```

## Section map (README headings)

1. Core Frameworks & Libraries (PyTorch, JAX, tinygrad, GGML, MLX…)
2. Model Codebases & Model Families
3. Inference Engines & Serving (vLLM, llama.cpp, TensorRT-LLM…)
4. Agentic AI & Multi-Agent Systems ← start here for agent builds
5. RAG & Knowledge (vector DBs, retrievers, chunking…)
6. Generative Media Tools
7. Training & Fine-tuning (LoRA/QLoRA, torchtune, axolotl…)
8. MLOps / LLMOps & Production
9. Evaluation, Benchmarks & Datasets
10. AI Safety, Alignment & Interpretability
11. Specialized Domains
12. User Interfaces & Self-hosted Platforms (Open WebUI, LibreChat…)
13. Developer Tools & Integrations
14. Resources & Learning

## Rules

- The list gives one-line verdicts per project — use them to shortlist 2-3,
  then verify against the project's own repo (API, license, maintenance status)
  before committing to it.
- Licenses vary per project (MIT/Apache-2.0 mostly, some copyleft or
  source-available). ALWAYS check the candidate's license against the user's
  commercial/open-source needs before recommending.
- Prefer actively maintained entries; distrust anything with no commit in 12+ months.
- For agentic coding work, combine: section 4 (agent framework) +
  section 3 (inference/serving) + section 5 (memory/RAG) + section 9 (evals).
