---
name: workflow-composer
description: "MANDATORY: Read this skill before planning or calling search, fetch, or agent when the current task needs its own research, browsing, or judgment for each of 5 or more independent, comparable items (10 or more: always fan out), or when the user asks for comprehensive coverage, parallel research, or subagents. Use `workflow/run` (the `run` tool on the `workflow` MCP server, called with the `mcp` tool using server: `workflow`, name: `run`) to compose those internal units: one dedicated agent per item, structured results aggregated back into the current task. Not for shortlists, one question with several facets, work a handful of searches can finish, or the same command over many inputs (write one script with bounded concurrency). Also use for loops, conditions, multi-stage map/reduce work, and deterministic subagent orchestration."
---

# Workflow Composer

`workflow/run` executes a deterministic JavaScript orchestration script that coordinates multiple subagents. The whole workflow runs as one background job; its return value is injected into the parent conversation when it finishes.

## When to Use
- The task contains 5 or more independent, comparable items processable concurrently (10 or more: always fan out).
- The user asks to research, compare, summarize, or analyze many entities with the same output structure.
- The outputs need to be collected into a table, report, ranking, dataset, or combined deliverable.
- Orchestration requires loops, conditions, retries, staged execution, aggregation, or dynamic fan-out.

## Decomposition & Map/Reduce Pattern
1. **Map**: Exactly one dedicated `agent()` call per independent item inside a `parallel()` group.
2. **Collect**: Keep successful structured results, record failures gracefully without crashing.
3. **Reduce**: Exactly one reducer agent over collected structured results to synthesize the comparison or final deliverable.
4. **Return**: Reducer output plus map results and explicit report paths.

## Execution Model
- Sandboxed deterministic JavaScript environment (no I/O, no Math.random(), no Date).
- Workflow completion acts as a barrier over every `agent()` call.
- Primitives:
  - `agent(prompt, {brief, schema, input_files, sandbox, effort_level})`
  - `parallel(brief, factory, {schema}?)`
  - `log(message)`
