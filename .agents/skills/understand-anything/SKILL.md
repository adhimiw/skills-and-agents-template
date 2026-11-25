---
name: understand-anything
description: Turn any codebase or repository into an interactive, visual knowledge graph using Egonex-AI/Understand-Anything. Use when onboarding to complex repositories, generating architecture diagrams, analyzing component dependencies, tracing business domain flows, and exploring systems visually.
allowed-tools: Read Write Edit Glob Grep
---

# Understand-Anything: Codebase Knowledge Graph & Architecture Visualizer

## Overview

`understand-anything` parses codebases into multi-dimensional knowledge graphs. Based on `Egonex-AI/Understand-Anything`, this skill combines static AST analysis, lexical dependency tracing, and agentic semantic comprehension to produce interactive, web-based architectural dashboards and navigable entity maps.

---

## Triggers & Activation Scenarios

Activate this skill when:
- Exploring unfamiliar repositories, legacy codebases, or multi-tier microservices.
- Visualizing data flows between frontend, API gateways, database layers, and background workers.
- Generating architecture diagrams, component trees, and domain models.
- Auditing call graphs, dead code paths, or circular dependencies.
- Preparing comprehensive onboarding guides and architectural decision records (ADRs).

---

## 1. Core Architecture Modes

| Mode | Command / Flag | Purpose |
| :--- | :--- | :--- |
| **`overview`** | `/understand` | High-level system topology, module boundaries, entry points |
| **`domain`** | `/understand-domain` | Business concepts, entity models, state machines, user flows |
| **`explain`** | `/understand-explain <sym>` | Deep-dive call graph and data dependencies for a specific file/function |
| **`diff`** | `/understand-diff` | Blast radius and impact analysis for uncommitted changes or PRs |
| **`dashboard`** | `/understand-dashboard` | Spawns interactive WebGL/Cytoscape node-graph viewer |

---

## 2. Standard Workflows

### 2.1 Indexing a Repository
```bash
# Generate static AST index and dependency map
understand index --path . --output ./docs/architecture-graph.json

# Launch local interactive dashboard
understand serve --port 4200
```

### 2.2 Domain Flow Extraction
```bash
# Map domain models and state transitions
understand domain --entrypoints src/index.ts,src/api/
```

### 2.3 Dependency Blast Radius Audit
```bash
# Trace inbound callers and downstream dependents
understand trace --symbol "auth_handler" --direction both
```
