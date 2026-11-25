# Full Skills & Agent Starter Template

A curated, dereferenced collection of **500 specialized AI agent skills** sorted by engineering work stream, paired with deterministic rules (`.agents/rules/`), instruction files (`AGENTS.md`, `GEMINI.md`, `DESIGN.md`), and verification tooling for **Google Antigravity, Claude Code, Cursor, Windsurf, and OpenCode**.

---

## Quick Jump by Work Type

| Work Area | Skills | Jump Link |
|---|---:|---|
| **1. AI Agents, LLMs, Gemini SDK & Skill Authoring** | 21 | [Browse](#1-ai-agents-llms-gemini-sdk-skill-authoring) |
| **2. Frontend UI/UX, Design Systems, Anti-Slop & 3D Web** | 42 | [Browse](#2-frontend-uiux-design-systems-anti-slop-3d-web) |
| **3. Architecture, Planning, Specs & Codebase Understanding** | 35 | [Browse](#3-architecture-planning-specs-codebase-understanding) |
| **4. Core Coding Discipline, Reviews & Issue Resolution** | 38 | [Browse](#4-core-coding-discipline-reviews-issue-resolution) |
| **5. Git Workflows, CI/CD, Performance & Production Shipping** | 15 | [Browse](#5-git-workflows-cicd-performance-production-shipping) |
| **6. QA Automation, Playwright, Browser Extraction & Debugging** | 27 | [Browse](#6-qa-automation-playwright-browser-extraction-debugging) |
| **7. Mobile Engineering (Flutter, Dart, Android & iOS)** | 28 | [Browse](#7-mobile-engineering-flutter-dart-android-ios) |
| **8. Cloud Backends & Firebase (Auth, Firestore & Functions)** | 12 | [Browse](#8-cloud-backends-firebase-auth-firestore-functions) |
| **9. Clean-Room Product Replication & Reverse Engineering** | 11 | [Browse](#9-clean-room-product-replication-reverse-engineering) |
| **10. Cybersecurity, AppSec Pentesting & Threat Response** | 39 | [Browse](#10-cybersecurity-appsec-pentesting-threat-response) |
| **11. Data Engineering, BigQuery, SQL Migration & Vertex AI** | 41 | [Browse](#11-data-engineering-bigquery-sql-migration-vertex-ai) |
| **12. Bioinformatics, Drug Discovery & Scientific Literature** | 51 | [Browse](#12-bioinformatics-drug-discovery-scientific-literature) |
| **13. Multimodal Vision, Video Intelligence & Audio Pipelines** | 8 | [Browse](#13-multimodal-vision-video-intelligence-audio-pipelines) |
| **14. Content, LinkedIn Growth, Slides & Document Tooling** | 30 | [Browse](#14-content-linkedin-growth-slides-document-tooling) |
| **15. Google Workspace Automation (`gws`), Recipes & Personas** | 95 | [Browse](#15-google-workspace-automation-gws-recipes-personas) |
| **16. Homelab, SSH Servers, Linux Desktop & Self-Hosting** | 7 | [Browse](#16-homelab-ssh-servers-linux-desktop-self-hosting) |

---

## Repository Structure

```text
skills-and-agents-template/
├── .agents/
│   ├── rules/        # Core guardrails (antislop, taste-skill, engineering-workflow, ui-ux)
│   └── skills/       # 500 dereferenced, self-contained SKILL.md modules
├── .claude/skills -> ../.agents/skills
├── skills -> .agents/skills
├── AGENTS.md         # Master workflow & skill index for coding agents
├── GEMINI.md         # Google Antigravity / Gemini instructions
├── DESIGN.md         # Editorial paper/ink design system baseline
└── package.json      # Validation & design helper scripts
```

---

## How to Use in Any Project

1. **Use an individual skill**: Copy any `.agents/skills/<skill-name>/` directory into your project’s `.agents/skills/` (or `~/.agents/skills/`) and read its `SKILL.md`.
2. **Bootstrap a full workspace**: Copy `.agents/`, `AGENTS.md`, `GEMINI.md`, and `.claude/` into your project root, run `npm install`, and instruct your agent:
   > *"Read `AGENTS.md` and use the relevant skills from `.agents/skills/` for this task."*
3. **Handy bundled CLI helpers**:
   - `npm run taste:draw -- --sector saas --brief "Your brief" --options 3` — Deal art direction blueprint
   - `npm run taste:inspect index.html` — Headless browser layout audit
   - `npm run taste:lint` — Anti-slop UI lint check
   - `npm run uiux:search "query" -- --domain style` — Search local UI/UX intelligence DB
   - `npm run a11y:contrast "#FFFFFF" "#0D1117"` — WCAG 2.2 AA/AAA contrast check

---

## Complete Skill Catalog (500 Skills Sorted by Work)

### 1. AI Agents, LLMs, Gemini SDK & Skill Authoring

*21 skills*

| Skill | Purpose / When to Use |
|---|---|
| [`agent-designer`](.agents/skills/agent-designer/SKILL.md) | Use when the user asks to design a multi-agent system, pick an orchestration pattern (supervisor/swarm/pipeline), generate tool schemas for agents, or evaluate ag... |
| [`agent-reach`](.agents/skills/agent-reach/SKILL.md) | MUST USE when user wants to research/search/look up/find anything on the internet — e.g. "research this topic", "do a deep dive on X", "search the web for X", "se... |
| [`awesome-oss-ai-dev`](.agents/skills/awesome-oss-ai-dev/SKILL.md) | Pick proven open-source AI building blocks for software work: LLM frameworks, inference engines, agent/multi-agent systems, RAG, eval harnesses, MLOps, UIs. Consu... |
| [`composio`](.agents/skills/composio/SKILL.md) | Use 1000+ external apps via Composio - either directly through the CLI or by building AI agents and apps with the SDK |
| [`find-skills`](.agents/skills/find-skills/SKILL.md) | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express inter... |
| [`gemini-api-cli`](.agents/skills/gemini-api-cli/SKILL.md) | Call the Gemini API from the shell with gemini-api. Use for media generation (images, TTS, music, video), file and YouTube analysis, audio/video transcription, De... |
| [`gemini-api-dev`](.agents/skills/gemini-api-dev/SKILL.md) | Use this skill when writing code that calls the Gemini API for text generation, multi-turn chat, multimodal understanding, image generation, video generation, spe... |
| [`gemini-live-api-dev`](.agents/skills/gemini-live-api-dev/SKILL.md) | Use this skill when building real-time, bidirectional streaming applications with the Gemini Live API, or migrating legacy Live models (2.0/2.5/3.1) to Gemini 3.8... |
| [`gemini-omni-flash-api`](.agents/skills/gemini-omni-flash-api/SKILL.md) | Use this skill for generative video editing, text-to-video, image- and video-referenced video generation, first-frame-to-video, first-and-last-frame transitions,... |
| [`google-antigravity-sdk`](.agents/skills/google-antigravity-sdk/SKILL.md) | Design, implement, and debug autonomous AI agents and multi-agent systems using the Google Antigravity (AGY) SDK. ACTIVATE this skill when the user wants to creat... |
| [`loop-me`](.agents/skills/loop-me/SKILL.md) | Grill me about specs for the workflows I want to build, within this workspace. |
| [`loopy`](.agents/skills/loopy/SKILL.md) | Discover, find, compare, audit, repair, adapt, craft, run, debrief, save, and prepare repeatable AI-agent loops for publication. Use when a user asks to analyze c... |
| [`mcp-server-builder`](.agents/skills/mcp-server-builder/SKILL.md) | Design and ship production-ready MCP (Model Context Protocol) servers from OpenAPI contracts instead of hand-written tool wrappers. Python and TypeScript support,... |
| [`mcptoon`](.agents/skills/mcptoon/SKILL.md) | Compress MCP tool discovery with the mcptoon CLI. Trigger when a session has a large MCP tool catalog (many servers/tools), when the user mentions token cost, too... |
| [`portfolio-agent-playbook`](.agents/skills/portfolio-agent-playbook/SKILL.md) | Operational playbook for connecting GitHub and LinkedIn OAuth locally into the AES-256-GCM MongoDB Env Vault via browser automation (chrome-mcp), running and veri... |
| [`portfolio-master`](.agents/skills/portfolio-master/SKILL.md) | Primary self-updating engineering skill for Adhithan's React 19 + MongoDB portfolio, mobile PWA resume app, encrypted DB Env Vault, GitHub/LinkedIn integrations,... |
| [`skill-creator`](.agents/skills/skill-creator/SKILL.md) | Trigger: new skills, agent instructions, documenting AI usage patterns. Create LLM-first skills with valid frontmatter. |
| [`skill-improver`](.agents/skills/skill-improver/SKILL.md) | Trigger: improve skills, audit skills, refactor skills, skill quality. Audit and upgrade existing LLM-first skills. |
| [`typesafe-ai`](.agents/skills/typesafe-ai/SKILL.md) | TypeSafe integration craft for System One models (sometimes called Decision Models) such as Jev, which answer typed questions about text, images, and application... |
| [`using-agent-skills`](.agents/skills/using-agent-skills/SKILL.md) | Discovers and invokes agent skills. Use when starting a session, or when you need to decide which skill or workflow applies to the piece of work at hand. This is... |
| [`workflow-composer`](.agents/skills/workflow-composer/SKILL.md) | MANDATORY: Read this skill before planning or calling search, fetch, or agent when the current task needs its own research, browsing, or judgment for each of 5 or... |

### 2. Frontend UI/UX, Design Systems, Anti-Slop & 3D Web

*42 skills*

| Skill | Purpose / When to Use |
|---|---|
| [`antislop`](.agents/skills/antislop/SKILL.md) | Anti Slop: Rules for AI Coding Agents. The core filter. Load always to stop generic AI slop. |
| [`antislop-code`](.agents/skills/antislop-code/SKILL.md) | Code comment hygiene for AI coding agents: remove generic AI-slop comments, keep the valuable ones, never touch the code. |
| [`antislop-copywriting`](.agents/skills/antislop-copywriting/SKILL.md) | Copy and text skill for antislop. Use when writing or editing prose: headlines, tone, CTAs, and anti-AI-writing patterns. Load with the core. |
| [`antislop-human`](.agents/skills/antislop-human/SKILL.md) | Human and accessibility skill for antislop. Contrast, keyboard, focus, and states for real people. Includes the contrast checker. |
| [`antislop-layoutmobile`](.agents/skills/antislop-layoutmobile/SKILL.md) | Mobile layout skill for antislop. Use for layouts that reflow across screen sizes, phone to desktop: grids, overflow, tap targets. Load with the core. |
| [`antislop-ui`](.agents/skills/antislop-ui/SKILL.md) | UI and visual skill for antislop. Use when building or editing any interface: color, layout, components, motion. Load with the core. |
| [`bencium-controlled-ux-designer`](.agents/skills/bencium-controlled-ux-designer/SKILL.md) | Expert UI/UX design guidance for unique, accessible interfaces. Use for visual decisions, colors, typography, layouts. Always ask before making design decisions.... |
| [`bencium-impact-designer`](.agents/skills/bencium-impact-designer/SKILL.md) | Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, or applicatio... |
| [`bencium-innovative-ux-designer`](.agents/skills/bencium-innovative-ux-designer/SKILL.md) | Develop an independent visual language and turn the human-chosen direction into a production-ready graphic, brand, campaign, publication, web, or product system.... |
| [`chrome-extensions`](.agents/skills/chrome-extensions/SKILL.md) | Build and publish Chrome Extensions using Manifest V3 best practices. Use this skill whenever the user asks to create, modify, debug, or understand Chrome browser... |
| [`composition-patterns`](.agents/skills/composition-patterns/SKILL.md) | React composition patterns that scale. Use when refactoring components with boolean prop proliferation, building flexible component libraries, or designing reusab... |
| [`design`](.agents/skills/design/SKILL.md) | Comprehensive design skill: brand identity, design tokens, UI styling, logo generation (55 styles, Gemini, Atlas Cloud, MuAPI, or UberLLM AI), corporate identity... |
| [`design-audit`](.agents/skills/design-audit/SKILL.md) | Premium UI/UX design audit and refinement skill. Conducts systematic visual audits of existing apps and produces phased, implementation-ready design plans. Use th... |
| [`design-system`](.agents/skills/design-system/SKILL.md) | Token architecture, component specifications, and slide generation. Three-layer tokens (primitive→semantic→component), CSS variables, spacing/typography scales, c... |
| [`design-taste-frontend`](.agents/skills/design-taste-frontend/SKILL.md) | tasteskill v2, the anti-slop frontend skill. Art direction for websites, distilled from a study of 247 curated gallery sites (One Page Love, Awwwards Sites of the... |
| [`design-taste-frontend-v1`](.agents/skills/design-taste-frontend-v1/SKILL.md) | The original taste-skill v1, kept for projects that depend on its exact behaviour. Opt-in: it runs only when called by name. |
| [`design-taste-frontend-v2-experimental`](.agents/skills/design-taste-frontend-v2-experimental/SKILL.md) | The single-file, dial-driven taste-skill that was the default before v2, kept for projects that depend on its exact behaviour. Opt-in: it runs only when called by... |
| [`diagram-design`](.agents/skills/diagram-design/SKILL.md) | Create branded architecture, architecture delta, IT current-state, flowchart, sequence, state machine, ER/data model, timeline, swimlane, quadrant, radar/spider,... |
| [`dioramas`](.agents/skills/dioramas/SKILL.md) | Build cinematic, interactive 3D websites and landing pages where a choreographed 3D scene carries the whole page. Uses Three.js r186, pmndrs postprocessing, N8AO,... |
| [`dioramas-3d-web`](.agents/skills/dioramas-3d-web/SKILL.md) | Build cinematic, interactive 3D websites and landing pages where a choreographed 3D scene carries the whole page. Uses Three.js r186, pmndrs postprocessing, N8AO,... |
| [`frontend-design`](.agents/skills/frontend-design/SKILL.md) | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography, and making choi... |
| [`frontend-ui-engineering`](.agents/skills/frontend-ui-engineering/SKILL.md) | Builds production-quality, accessible, responsive user-facing UIs. Use when building or modifying interfaces and pages, creating components, implementing layouts,... |
| [`gpt-taste`](.agents/skills/gpt-taste/SKILL.md) | Classic skill for GPT and Codex, opt-in: it runs only when called by name. Layout variance, a strict AIDA page structure and GSAP scroll motion. |
| [`high-end-visual-design`](.agents/skills/high-end-visual-design/SKILL.md) | Classic style skill, opt-in: it runs only when called by name. A calm, polished look with soft contrast, generous whitespace and spring motion. |
| [`image-to-code`](.agents/skills/image-to-code/SKILL.md) | Moved to github.com/Leonxlnx/imagegen-skills. Runs only when called by name. |
| [`imagegen-frontend-mobile`](.agents/skills/imagegen-frontend-mobile/SKILL.md) | Moved to github.com/Leonxlnx/imagegen-skills. Runs only when called by name. |
| [`imagegen-frontend-web`](.agents/skills/imagegen-frontend-web/SKILL.md) | Moved to github.com/Leonxlnx/imagegen-skills. Runs only when called by name. |
| [`impeccable`](.agents/skills/impeccable/SKILL.md) | Use when the user wants to design, redesign, shape, critique, audit, polish, simplify, harden, animate, or otherwise improve a frontend interface: websites, landi... |
| [`industrial-brutalist-ui`](.agents/skills/industrial-brutalist-ui/SKILL.md) | Classic style skill, opt-in: it runs only when called by name. A hard mechanical look with Swiss type, rigid grids, extreme scale contrast and utilitarian colour. |
| [`make-interfaces-feel-better`](.agents/skills/make-interfaces-feel-better/SKILL.md) | Design engineering principles for making interfaces feel polished. Use when building UI components, reviewing frontend code, implementing animations, hover states... |
| [`minimalist-ui`](.agents/skills/minimalist-ui/SKILL.md) | Classic style skill, opt-in: it runs only when called by name. Editorial product UI with a warm monochrome palette, typographic contrast and flat bento grids. |
| [`modern-web-guidance`](.agents/skills/modern-web-guidance/SKILL.md) | Search tool for modern web development best practices. MANDATORY: Execute FIRST for all HTML/CSS and clientside JS tasks. Do NOT skip — web APIs evolve rapidly an... |
| [`react-best-practices`](.agents/skills/react-best-practices/SKILL.md) | React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js cod... |
| [`react-view-transitions`](.agents/skills/react-view-transitions/SKILL.md) | Guide for implementing smooth, native-feeling animations using React's View Transition API ('<ViewTransition>' component, 'addTransitionType', and CSS view transi... |
| [`redesign-existing-projects`](.agents/skills/redesign-existing-projects/SKILL.md) | Retired: redesigns, restyles and design reviews are part of design-taste-frontend. Runs only when called by name. |
| [`stitch-design-taste`](.agents/skills/stitch-design-taste/SKILL.md) | Classic skill for Google Stitch, opt-in: it runs only when called by name. Writes an agent-friendly DESIGN.md with strict type, colour and layout rules. |
| [`taste-skill`](.agents/skills/taste-skill/SKILL.md) | tasteskill v2, the anti-slop frontend skill. Art direction for websites, distilled from a study of 247 curated gallery sites (One Page Love, Awwwards Sites of the... |
| [`typography`](.agents/skills/typography/SKILL.md) | Professional typography rules for UI design, web applications, software interfaces, and all screen-based text. Enforces timeless typographic correctness that LLMs... |
| [`ui-styling`](.agents/skills/ui-styling/SKILL.md) | Create beautiful, accessible user interfaces with shadcn/ui components (built on Radix UI + Tailwind), Tailwind CSS utility-first styling, and canvas-based visual... |
| [`ui-ux-pro-max`](.agents/skills/ui-ux-pro-max/SKILL.md) | UI/UX design intelligence for web, mobile, and desktop. This skill should be used when designing, building, reviewing, or fixing interfaces, including pages, comp... |
| [`ux-writing`](.agents/skills/ux-writing/SKILL.md) | Create user-centered, accessible interface copy (microcopy) for digital products including buttons, labels, error messages, notifications, forms, onboarding, empt... |
| [`web-design-guidelines`](.agents/skills/web-design-guidelines/SKILL.md) | Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site ag... |

### 3. Architecture, Planning, Specs & Codebase Understanding

*35 skills*

| Skill | Purpose / When to Use |
|---|---|
| [`api-and-interface-design`](.agents/skills/api-and-interface-design/SKILL.md) | Guides stable API and interface design. Use when designing APIs, module boundaries, or any public interface. Use when creating REST or GraphQL endpoints, defining... |
| [`codebase-design`](.agents/skills/codebase-design/SKILL.md) | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportunities, decide where a seam... |
| [`codebase-memory`](.agents/skills/codebase-memory/SKILL.md) | Use the codebase knowledge graph for structural code queries. Triggers on: explore the codebase, understand the architecture, what functions exist, show me the st... |
| [`constraint-driven-development`](.agents/skills/constraint-driven-development/SKILL.md) | Establishes a project's quality bar as a written contract and stops agents quietly lowering it. Interviews the user on which dimensions matter, supplies sane defa... |
| [`context-engineering`](.agents/skills/context-engineering/SKILL.md) | Optimizes agent context setup. Use when starting a new session, when agent output quality degrades, when switching between tasks, or when you need to configure ru... |
| [`domain-modeling`](.agents/skills/domain-modeling/SKILL.md) | Build and sharpen a project's domain model. Use when discussing codebase terminology, writing or editing a GLOSSARY.md, or recording or editing an ADR. |
| [`grill-me`](.agents/skills/grill-me/SKILL.md) | A relentless interview to sharpen a plan or design. |
| [`grill-with-docs`](.agents/skills/grill-with-docs/SKILL.md) | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. |
| [`grilling`](.agents/skills/grilling/SKILL.md) | Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases. |
| [`idea-refine`](.agents/skills/idea-refine/SKILL.md) | Refines raw ideas into sharp, actionable concepts through structured divergent and convergent thinking. Use when an idea is still vague, when you need to stress-t... |
| [`improve-codebase-architecture`](.agents/skills/improve-codebase-architecture/SKILL.md) | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. |
| [`interview-me`](.agents/skills/interview-me/SKILL.md) | Extracts what the user actually wants instead of what they think they should want. Achieves this through one-question-at-a-time interview until ~95% confidence ab... |
| [`planning-and-task-breakdown`](.agents/skills/planning-and-task-breakdown/SKILL.md) | Breaks work into ordered tasks. Use when you have a spec or clear requirements and need to break work into implementable tasks. Use when a task feels too large to... |
| [`prototype`](.agents/skills/prototype/SKILL.md) | Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check whether a state model or logic feels right, or explore what a UI... |
| [`rea`](.agents/skills/rea/SKILL.md) | Reverse Engineer Anything (REA) analysis engine based on morluto/rea. Use when analyzing compiled binaries, disassembling native code, decompiling Android APKs, i... |
| [`rederive`](.agents/skills/rederive/SKILL.md) | Teaches a codebase by making the user re-derive its design decisions from first principles through Socratic questions, instead of explaining the code. Works on th... |
| [`research`](.agents/skills/research/SKILL.md) | Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the user wants a topic researched, doc... |
| [`reverse-engineer-anything`](.agents/skills/reverse-engineer-anything/SKILL.md) | Reverse engineer native, managed, Electron/JavaScript, packaged, firmware, and browser targets with REA. Use shipped-artifact or requested runtime evidence to exp... |
| [`source-driven-development`](.agents/skills/source-driven-development/SKILL.md) | Grounds every implementation decision in official documentation. Use when you want to verify an approach against the official docs before implementing it, or when... |
| [`spec-driven-development`](.agents/skills/spec-driven-development/SKILL.md) | Creates specs before coding. Use when starting a new project, feature, or significant change and no specification exists yet. Use when drafting a PRD or requireme... |
| [`to-questionnaire`](.agents/skills/to-questionnaire/SKILL.md) | Turn a decision you can't fully answer into a questionnaire for someone else to fill in. |
| [`to-spec`](.agents/skills/to-spec/SKILL.md) | Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already discussed. |
| [`to-tickets`](.agents/skills/to-tickets/SKILL.md) | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured tracker (edges... |
| [`understand`](.agents/skills/understand/SKILL.md) | Analyze a codebase to produce an interactive knowledge graph for understanding architecture, components, and relationships |
| [`understand-anything`](.agents/skills/understand-anything/SKILL.md) | Turn any codebase or repository into an interactive, visual knowledge graph using Egonex-AI/Understand-Anything. Use when onboarding to complex repositories, gene... |
| [`understand-chat`](.agents/skills/understand-chat/SKILL.md) | Use when you need to ask questions about a codebase or understand code using a knowledge graph |
| [`understand-dashboard`](.agents/skills/understand-dashboard/SKILL.md) | Launch the interactive web dashboard to visualize a codebase's knowledge graph |
| [`understand-diff`](.agents/skills/understand-diff/SKILL.md) | Use when you need to analyze git diffs or pull requests to understand what changed, affected components, and risks |
| [`understand-domain`](.agents/skills/understand-domain/SKILL.md) | Extract business domain knowledge from a codebase and generate an interactive domain flow graph. Works standalone (lightweight scan) or derives from an existing /... |
| [`understand-explain`](.agents/skills/understand-explain/SKILL.md) | Use when you need a deep-dive explanation of a specific file, function, or module in the codebase |
| [`understand-figma`](.agents/skills/understand-figma/SKILL.md) | Analyze a Figma file via the Figma REST API and generate an interactive design knowledge graph (pages, screens, components, component sets, instances, design toke... |
| [`understand-knowledge`](.agents/skills/understand-knowledge/SKILL.md) | Analyze a Karpathy-pattern LLM wiki knowledge base and generate an interactive knowledge graph with entity extraction, implicit relationships, and topic clustering. |
| [`understand-onboard`](.agents/skills/understand-onboard/SKILL.md) | Use when you need to generate an onboarding guide for new team members joining a project |
| [`wait-what`](.agents/skills/wait-what/SKILL.md) | Stop. That last message did not land: re-pitch it. |
| [`wayfinder`](.agents/skills/wayfinder/SKILL.md) | Plan a huge chunk of work (more than one agent session can hold) as a shared map of decision tickets on your issue tracker, and resolve them one at a time until t... |

### 4. Core Coding Discipline, Reviews & Issue Resolution

*38 skills*

| Skill | Purpose / When to Use |
|---|---|
| [`adversarial-reviewer`](.agents/skills/adversarial-reviewer/SKILL.md) | Adversarial code review that breaks the self-review monoculture. Use when you want a genuinely critical review of recent changes, before merging a PR, or when you... |
| [`api-design-reviewer`](.agents/skills/api-design-reviewer/SKILL.md) | Comprehensive REST API design review with automated linting, breaking-change detection, and design scorecards. Catches inconsistent conventions, missing versionin... |
| [`ask-matt`](.agents/skills/ask-matt/SKILL.md) | Ask which skill or flow fits your situation. A router over the skills in this repo. |
| [`chief-of-staff`](.agents/skills/chief-of-staff/SKILL.md) | Pursue a long-running goal in a single session by co-ordinating subagents. |
| [`cli-hub-meta-skill`](.agents/skills/cli-hub-meta-skill/SKILL.md) | Discover agent-native CLIs for professional software. Access the live catalog to find tools for creative workflows, productivity, AI, and more. |
| [`code-review`](.agents/skills/code-review/SKILL.md) | Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes: Standards (does the code follow this repo's documented coding standard... |
| [`code-review-and-quality`](.agents/skills/code-review-and-quality/SKILL.md) | Conducts multi-axis code review. Use before merging any change. Use when reviewing code written by yourself, another agent, or a human. Use when you need to asses... |
| [`code-simplification`](.agents/skills/code-simplification/SKILL.md) | Simplifies code for clarity. Use when refactoring code for clarity without changing behavior. Use when code works but is harder to read, maintain, or extend than... |
| [`deprecation-and-migration`](.agents/skills/deprecation-and-migration/SKILL.md) | Manages deprecation and migration. Use when removing old systems, APIs, or features. Use when migrating users from one implementation to another. Use when migrati... |
| [`doubt-driven-development`](.agents/skills/doubt-driven-development/SKILL.md) | Subjects every non-trivial decision to a fresh-context adversarial review before it stands. Use when you want every assumption cross-examined before proceeding, w... |
| [`exploiting-server-side-request-forgery`](.agents/skills/exploiting-server-side-request-forgery/SKILL.md) | Identifying and exploiting SSRF vulnerabilities to access internal services, cloud metadata, and restricted network resources during authorized penetration tests. |
| [`exploiting-template-injection-vulnerabilities`](.agents/skills/exploiting-template-injection-vulnerabilities/SKILL.md) | Detects and exploits Server-Side Template Injection (SSTI) vulnerabilities across Jinja2, Twig, Freemarker, and other template engines to achieve remote code exec... |
| [`exploiting-websocket-vulnerabilities`](.agents/skills/exploiting-websocket-vulnerabilities/SKILL.md) | Testing WebSocket implementations for authentication bypass, cross-site hijacking, injection attacks, and insecure message handling during authorized security ass... |
| [`focused-fix`](.agents/skills/focused-fix/SKILL.md) | Use when the user asks to fix, debug, or make a specific feature/module/area work end-to-end. Triggers: 'make X work', 'fix the Y feature', 'the Z module is broke... |
| [`genie-4-live-world`](.agents/skills/genie-4-live-world/SKILL.md) | Use this skill when building real-time interactive world generation and simulation apps with Genie 4 (models/genie-4) over the Live Interactions API (interactions... |
| [`gentle-ai-bench`](.agents/skills/gentle-ai-bench/SKILL.md) | Trigger: bench, journey, journeys, driven mode, gentle-ai-bench, journey corpus, j-numbers, bench axis. Author and verify gentle-ai bench journeys; go test ./benc... |
| [`gentle-ai-collab-perfect`](.agents/skills/gentle-ai-collab-perfect/SKILL.md) | Trigger: contributing to Gentleman-Programming/gentle-ai as an external collaborator. Strict issue-first workflow, honest PR bodies, contributor-vs-maintainer sco... |
| [`gravitas`](.agents/skills/gravitas/SKILL.md) | Use for software implementation, debugging, refactoring, review, migration, and other repository-changing engineering work where correctness must be verified. Enf... |
| [`gravitas-highstakes`](.agents/skills/gravitas-highstakes/SKILL.md) | Mandatory checkpoint skill for irreversible/high-stakes changes (schema migrations, file deletion, auth/security changes, production config, force-pushes). Use wh... |
| [`gravitas-python`](.agents/skills/gravitas-python/SKILL.md) | GRAVITAS extension for Python projects. Adds Python-specific recon, type checking with mypy/pyright, ruff/flake8 lint, pytest patterns, and common Python failure... |
| [`gravitas-typescript`](.agents/skills/gravitas-typescript/SKILL.md) | GRAVITAS extension for TypeScript projects. Adds TypeScript-specific recon, strict mode patterns, Vitest/Jest integration, and common TS failure modes. Load in ad... |
| [`implement`](.agents/skills/implement/SKILL.md) | Implement a piece of work based on a spec or set of tickets. |
| [`implement-spec`](.agents/skills/implement-spec/SKILL.md) | Implement the result of /to-spec and /to-tickets in code. |
| [`incremental-implementation`](.agents/skills/incremental-implementation/SKILL.md) | Delivers changes incrementally in thin, verifiable slices. Use when implementing any feature or change that touches more than one file, or when picking up the nex... |
| [`issue-creation`](.agents/skills/issue-creation/SKILL.md) | Trigger: issue creation, bug reports, feature requests, or issue approval. Create and triage GitHub issues from repository evidence. |
| [`issue-root-resolution`](.agents/skills/issue-root-resolution/SKILL.md) | Trigger: root audit, atacar la raíz, issue roots, backlog roots, mechanism map, deletion-driven fix, resolver issues de raíz, close outdated issues. Audit and res... |
| [`judgment-day`](.agents/skills/judgment-day/SKILL.md) | Trigger: judgment day, dual review, adversarial review, juzgar. Run explicit blind dual review with at most two scoped fix/re-judgment rounds. |
| [`learning-from-mistakes`](.agents/skills/learning-from-mistakes/SKILL.md) | The user corrected an answer about a video — "no, it actually says X", "that's the wrong timestamp", "you misread the error code" — or asks why a video answer was... |
| [`retro`](.agents/skills/retro/SKILL.md) | Conduct a retrospective on a coding session. |
| [`scaffold-exercises`](.agents/skills/scaffold-exercises/SKILL.md) | Create exercise directory structures with sections, problems, solutions, and explainers that pass linting. Use when user wants to scaffold exercises, create exerc... |
| [`self-eval`](.agents/skills/self-eval/SKILL.md) | Honestly evaluate AI work quality using a two-axis scoring system. Use after completing a task, code review, or work session to get an unbiased assessment. Detect... |
| [`setup-matt-pocock-skills`](.agents/skills/setup-matt-pocock-skills/SKILL.md) | Configure this repo for the engineering skills: set up its issue tracker, triage label vocabulary, and domain doc layout. Run once before first use of the other e... |
| [`setup-ts-deep-modules`](.agents/skills/setup-ts-deep-modules/SKILL.md) | Wire dependency-cruiser into a TypeScript repo so each package is a deep module, with implementation hidden in subfolders and reachable only through its entry-poi... |
| [`sharing-results`](.agents/skills/sharing-results/SKILL.md) | The user wants to share or hand off what was found in a video — "send this analysis to my team", "make a page I can share", "export the findings", "give me someth... |
| [`systemic-issue-triage`](.agents/skills/systemic-issue-triage/SKILL.md) | Trigger: new issue, bug report, triage, backlog, issue flood, community report, root cause, dead-end, blocked user. Attack issues by root class, never one-by-one;... |
| [`teach`](.agents/skills/teach/SKILL.md) | Teach the user a new skill or concept, within this workspace. |
| [`testing-for-json-web-token-vulnerabilities`](.agents/skills/testing-for-json-web-token-vulnerabilities/SKILL.md) | Tests JWT implementations for algorithm confusion, "none" algorithm bypass, kid/jku parameter injection, and weak secret exploitation using jwt_tool and Burp Suit... |
| [`triage`](.agents/skills/triage/SKILL.md) | Move issues and external PRs through a state machine of triage roles, categorise, verify, grill if needed, and write agent-ready briefs. |

### 5. Git Workflows, CI/CD, Performance & Production Shipping

*15 skills*

| Skill | Purpose / When to Use |
|---|---|
| [`branch-pr`](.agents/skills/branch-pr/SKILL.md) | Create Gentle AI pull requests with issue-first checks. Trigger: creating, opening, or preparing PRs for review. |
| [`chained-pr`](.agents/skills/chained-pr/SKILL.md) | Trigger: PRs over 400 lines, stacked PRs, review slices. Split oversized changes into chained PRs that protect review focus. |
| [`ci-cd-and-automation`](.agents/skills/ci-cd-and-automation/SKILL.md) | Automates CI/CD pipeline setup. Use when setting up or modifying build and deployment pipelines. Use when you need to automate quality gates, configure test runne... |
| [`claude-handoff`](.agents/skills/claude-handoff/SKILL.md) | Hand the current conversation off to a fresh background agent that picks up the work immediately. |
| [`git-guardrails-claude-code`](.agents/skills/git-guardrails-claude-code/SKILL.md) | Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. Use when user wants to prevent destruct... |
| [`git-workflow`](.agents/skills/git-workflow/SKILL.md) | Advanced Git workflows and version control practices based on iuliandita/skills/git. Covers atomic commits with interactive staging, rebase workflows with autosqu... |
| [`git-workflow-and-versioning`](.agents/skills/git-workflow-and-versioning/SKILL.md) | Structures git workflow practices. Use when making any code change. Use when committing, branching, resolving conflicts, splitting uncommitted work in a messy wor... |
| [`handoff`](.agents/skills/handoff/SKILL.md) | Compact the current conversation into a handoff document for another agent to pick up. |
| [`observability-and-instrumentation`](.agents/skills/observability-and-instrumentation/SKILL.md) | Instruments code so production behavior is visible and diagnosable. Use when adding logging, metrics, tracing, or alerting. Use when shipping any feature that run... |
| [`performance-optimization`](.agents/skills/performance-optimization/SKILL.md) | Optimizes application performance across frontend, backend, queries, and databases. Use when performance requirements exist, when you suspect performance regressi... |
| [`pr`](.agents/skills/pr/SKILL.md) | Use when writing a PR body. |
| [`ship-gate`](.agents/skills/ship-gate/SKILL.md) | Pre-production audit that scans a codebase for security, database, deployment, code quality, AI/LLM, dependency, frontend, and observability issues. Intercepts de... |
| [`shipping-and-launch`](.agents/skills/shipping-and-launch/SKILL.md) | Prepares production launches. Use when preparing to deploy to production, or when asking what needs to be in place before shipping. Use when you need a pre-launch... |
| [`wizard`](.agents/skills/wizard/SKILL.md) | Generate an interactive bash wizard that walks a human through steps only they can perform. Use when provisioning infrastructure, setting up credentials or CI sec... |
| [`work-unit-commits`](.agents/skills/work-unit-commits/SKILL.md) | Plan commits as reviewable work units. Trigger: implementation, commit splitting, chained PRs, or keeping tests and docs with code. |

### 6. QA Automation, Playwright, Browser Extraction & Debugging

*27 skills*

| Skill | Purpose / When to Use |
|---|---|
| [`a11y-debugging`](.agents/skills/a11y-debugging/SKILL.md) | Uses Chrome DevTools MCP for accessibility (a11y) debugging and auditing based on web.dev guidelines. Use when testing semantic HTML, ARIA labels, focus states, k... |
| [`accessibility-audit`](.agents/skills/accessibility-audit/SKILL.md) | Whole site or product — a full web accessibility (a11y) audit against WCAG 2.2, following the WCAG-EM methodology. Defines scope, samples representative pages and... |
| [`accessibility-fix`](.agents/skills/accessibility-fix/SKILL.md) | Remediation only — repair web accessibility (a11y) violations against WCAG 2.2 with a baseline, edit, and verify loop. Takes a target (URL, files, directory) or a... |
| [`accessibility-inspect`](.agents/skills/accessibility-inspect/SKILL.md) | One page, hands-on manual tier — drive a live page through the web accessibility (a11y) checks a rule engine can't decide: keyboard operation and focus order, scr... |
| [`accessibility-scan`](.agents/skills/accessibility-scan/SKILL.md) | One page, automated tier — run the web accessibility (a11y) rule engine against a live page and locate every violation it can detect mechanically. Pass a URL, a c... |
| [`audit-website`](.agents/skills/audit-website/SKILL.md) | Audit a website with the squirrelscan CLI and fix the findings in code. Runs SEO, performance, security, technical, content, accessibility, and 16 other rule cate... |
| [`browser-harness`](.agents/skills/browser-harness/SKILL.md) | Control a real browser via CDP: clicking, typing, navigation, logged-in sessions, JS-rendered or bot-protected pages. Not for plain HTTP fetches of public content... |
| [`browser-testing-with-devtools`](.agents/skills/browser-testing-with-devtools/SKILL.md) | Tests in real browsers via Chrome DevTools MCP. Use when building or debugging anything that runs in a browser. Use when you need to inspect the DOM, capture cons... |
| [`chrome-devtools`](.agents/skills/chrome-devtools/SKILL.md) | Uses Chrome DevTools via MCP for efficient debugging, troubleshooting and browser automation. Use when debugging web pages, automating browser interactions, analy... |
| [`cookie-debugging`](.agents/skills/cookie-debugging/SKILL.md) | Uses Chrome DevTools MCP for inspecting, debugging, and testing cookies, session state, authentication issues, and cookie consent compliance. Use when diagnosing... |
| [`debug-optimize-lcp`](.agents/skills/debug-optimize-lcp/SKILL.md) | Guides debugging and optimizing Largest Contentful Paint (LCP) using Chrome DevTools MCP tools. Use this skill whenever the user asks about LCP performance, slow... |
| [`debugging-and-error-recovery`](.agents/skills/debugging-and-error-recovery/SKILL.md) | Guides systematic root-cause debugging. Use when tests fail, builds break, something that worked yesterday broke, behavior doesn't match expectations, or you enco... |
| [`defuddle`](.agents/skills/defuddle/SKILL.md) | Extract clean Markdown from HTML pages with Defuddle CLI. |
| [`diagnose-crash`](.agents/skills/diagnose-crash/SKILL.md) | Diagnose why a program crashed on this machine, from a systemd-coredump core dump. Use when a process has segfaulted, aborted, or otherwise dumped core, when aske... |
| [`diagnosing-bugs`](.agents/skills/diagnosing-bugs/SKILL.md) | Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow. |
| [`lightpanda-browser`](.agents/skills/lightpanda-browser/SKILL.md) | Ultra-fast, low-memory Zig-based headless browser automation for AI agents. Covers Lightpanda binary and Docker setup, Chrome DevTools Protocol (CDP) integration... |
| [`memory-leak-debugging`](.agents/skills/memory-leak-debugging/SKILL.md) | Diagnoses and resolves memory leaks in JavaScript/Node.js applications. Use when a user reports high memory usage, OOM errors, or wants to capture, compare, or in... |
| [`migrate-to-shoehorn`](.agents/skills/migrate-to-shoehorn/SKILL.md) | Migrate test files from 'as' type assertions to @total-typescript/shoehorn. Use when user mentions shoehorn, wants to replace 'as' in tests, or needs partial test... |
| [`playwright-skill`](.agents/skills/playwright-skill/SKILL.md) | Complete browser automation with Playwright. Auto-detects dev servers, writes reusable test scripts, and supports screenshots, responsive checks, UX validation, l... |
| [`recovering-from-errors`](.agents/skills/recovering-from-errors/SKILL.md) | A Watch Skill command failed, video download broke, ffmpeg or yt-dlp is missing, a provider returned an error, local vision stopped, or the user asks "why can't i... |
| [`scrapling`](.agents/skills/scrapling/SKILL.md) | Scrape web pages using Scrapling with HTTP requests, stealth browsers, JavaScript rendering, browser actions, API response capture, concurrent spiders, and adapti... |
| [`setup-pre-commit`](.agents/skills/setup-pre-commit/SKILL.md) | Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when user wants to add pre-commit hooks, set up Husky... |
| [`skill-tester`](.agents/skills/skill-tester/SKILL.md) | Validate, test, and score the quality of skills within the claude-skills ecosystem. Comprehensive meta-skill: structure validation, Python script testing (syntax... |
| [`tdd`](.agents/skills/tdd/SKILL.md) | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests. |
| [`test-driven-development`](.agents/skills/test-driven-development/SKILL.md) | Drives development with tests using the red-green-refactor loop. Use when implementing any logic, fixing any bug, or changing any behavior. Use when you need to p... |
| [`troubleshooting`](.agents/skills/troubleshooting/SKILL.md) | Uses Chrome DevTools MCP and documentation to troubleshoot connection and target issues. Trigger this skill when list_pages, new_page, or navigate_page fail, or w... |
| [`webapp-testing`](.agents/skills/webapp-testing/SKILL.md) | Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing brow... |

### 7. Mobile Engineering (Flutter, Dart, Android & iOS)

*28 skills*

| Skill | Purpose / When to Use |
|---|---|
| [`compose-preview`](.agents/skills/compose-preview/SKILL.md) | Instructions for the Android Compose Preview sidecar, which renders Jetpack Compose @Preview functions with 'android preview render' and shows them in the Android... |
| [`dart-add-unit-test`](.agents/skills/dart-add-unit-test/SKILL.md) | Write and organize unit tests for functions, methods, and classes using 'package:test'. Use when creating new logic or fixing bugs to ensure code remains correct... |
| [`dart-build-cli-app`](.agents/skills/dart-build-cli-app/SKILL.md) | Architectural patterns, entrypoint structure, exit codes, stream routing, and subprocess spawning for Dart command-line interface (CLI) applications. Use when bui... |
| [`dart-collect-coverage`](.agents/skills/dart-collect-coverage/SKILL.md) | Collect coverage using the coverage packge and create an LCOV report |
| [`dart-fix-runtime-errors`](.agents/skills/dart-fix-runtime-errors/SKILL.md) | Uses get_runtime_errors and lsp to fetch an active stack trace, locate the failing line, apply a fix, and verify resolution via hot_reload. |
| [`dart-generate-test-mocks`](.agents/skills/dart-generate-test-mocks/SKILL.md) | Define and generate mock objects for external dependencies using 'package:mockito' and 'build_runner'. Use when unit testing classes that depend on complex extern... |
| [`dart-migrate-to-checks-package`](.agents/skills/dart-migrate-to-checks-package/SKILL.md) | Replace the usage of 'expect' and similar functions from 'package:matcher' to 'package:checks' equivalents. |
| [`dart-resolve-package-conflicts`](.agents/skills/dart-resolve-package-conflicts/SKILL.md) | Workflow for fixing package version conflicts. Use this when 'pub get' fails due to incompatible package versions. |
| [`dart-run-static-analysis`](.agents/skills/dart-run-static-analysis/SKILL.md) | Execute 'dart analyze' to identify warnings and errors, and use 'dart fix --apply' to automatically resolve mechanical lint issues. Use during development to ensu... |
| [`dart-setup-ffi-assets`](.agents/skills/dart-setup-ffi-assets/SKILL.md) | Guides agents in compiling and packaging C/C++ source code into dynamic or static libraries (Code Assets) using Dart's Native Assets hook system (via hook/build.d... |
| [`dart-use-doc-examples`](.agents/skills/dart-use-doc-examples/SKILL.md) | How to inject external code examples into Dartdoc using the {@example} directive, and how to filter those files using #hide, #region, and #endregion tags. |
| [`dart-use-ffigen`](.agents/skills/dart-use-ffigen/SKILL.md) | Guide agents to use 'package:ffigen' to automatically generate FFI bindings instead of writing them manually. Use this skill when a task involves writing new FFI... |
| [`dart-use-path-package`](.agents/skills/dart-use-path-package/SKILL.md) | Cross-platform file and directory path manipulation, segment splitting, extension extraction, and context conversion using 'package:path' and 'package:file'. Use... |
| [`dart-use-pattern-matching`](.agents/skills/dart-use-pattern-matching/SKILL.md) | Applies Dart 3 pattern matching, switch expressions, and destructuring idiomatically to validate data schemas, handle algebraic data types, and decompose control... |
| [`dart-use-primary-constructors`](.agents/skills/dart-use-primary-constructors/SKILL.md) | Help users write syntactically and semantically correct primary constructors in Dart, and migrate/use the new constructor syntax, empty-body semicolon syntax, in-... |
| [`dart-write-documentation`](.agents/skills/dart-write-documentation/SKILL.md) | Rules and formatting guidelines for writing Dart /// API documentation and doc comments. Use when documenting Dart code, writing doc comments for any Dart declara... |
| [`device-hub`](.agents/skills/device-hub/SKILL.md) | Instructions for working with the Android Device Hub sidecar, which lists, starts, stops, creates and removes Android Virtual Devices (AVDs), lists physical devic... |
| [`flutter-add-integration-test`](.agents/skills/flutter-add-integration-test/SKILL.md) | Configures Flutter Driver for app interaction and converts MCP actions into permanent integration tests. Use when adding integration testing to a project, explori... |
| [`flutter-add-widget-preview`](.agents/skills/flutter-add-widget-preview/SKILL.md) | Adds interactive widget previews to the project using the previews.dart system. Use when creating new UI components or updating existing screens to ensure consist... |
| [`flutter-add-widget-test`](.agents/skills/flutter-add-widget-test/SKILL.md) | Implement a component-level test using 'WidgetTester' to verify UI rendering and user interactions (tapping, scrolling, entering text). Use when validating that a... |
| [`flutter-apply-architecture-best-practices`](.agents/skills/flutter-apply-architecture-best-practices/SKILL.md) | Architects a Flutter application using the recommended layered approach (UI, Logic, Data). Use when structuring a new project or refactoring for scalability. |
| [`flutter-build-responsive-layout`](.agents/skills/flutter-build-responsive-layout/SKILL.md) | Use 'LayoutBuilder', 'MediaQuery', or 'Expanded/Flexible' to create a layout that adapts to different screen sizes. Use when you need the UI to look good on both... |
| [`flutter-fix-layout-issues`](.agents/skills/flutter-fix-layout-issues/SKILL.md) | Fixes Flutter layout errors (overflows, unbounded constraints) using Dart and Flutter MCP tools. Use when addressing "RenderFlex overflowed", "Vertical viewport w... |
| [`flutter-implement-json-serialization`](.agents/skills/flutter-implement-json-serialization/SKILL.md) | Create model classes with 'fromJson' and 'toJson' methods using 'dart:convert'. Use when manually mapping JSON keys to class properties for simple data structures. |
| [`flutter-setup-declarative-routing`](.agents/skills/flutter-setup-declarative-routing/SKILL.md) | Configure 'MaterialApp.router' using a package like 'go_router' for advanced URL-based navigation. Use when developing web applications or mobile apps that requir... |
| [`flutter-setup-localization`](.agents/skills/flutter-setup-localization/SKILL.md) | Add 'flutter_localizations' and 'intl' dependencies, enable "generate true" in 'pubspec.yaml', and create an 'l10n.yaml' configuration file. Use when initializing... |
| [`flutter-use-http-package`](.agents/skills/flutter-use-http-package/SKILL.md) | Use the 'http' package to execute GET, POST, PUT, or DELETE requests. Use when you need to fetch from or send data to a REST API. |
| [`xcode_project_setup`](.agents/skills/xcode_project_setup/SKILL.md) | Safely modifies Xcode projects (.pbxproj) to add Swift Packages and link files. Use this skill whenever an iOS project needs dependencies installed (e.g. Firebase... |

### 8. Cloud Backends & Firebase (Auth, Firestore & Functions)

*12 skills*

| Skill | Purpose / When to Use |
|---|---|
| [`extension_to_functions_codebase`](.agents/skills/extension_to_functions_codebase/SKILL.md) | Skill for converting an installed Firebase Extension (or extension source) into a standalone Cloud Functions for Firebase codebase or publishable npm package, inc... |
| [`firebase_ai_logic_basics`](.agents/skills/firebase_ai_logic_basics/SKILL.md) | Official skill for integrating Firebase AI Logic (Gemini API) into web applications. Covers setup, multimodal inference, structured output, and security. |
| [`firebase_app_hosting_basics`](.agents/skills/firebase_app_hosting_basics/SKILL.md) | Deploys and manages full-stack web applications (Next.js, Angular) with Server-Side Rendering (SSR) using Firebase App Hosting. Use when deploying Next.js/Angular... |
| [`firebase_auth_basics`](.agents/skills/firebase_auth_basics/SKILL.md) | Guide for setting up and using Firebase Authentication. Use this skill when the user's app requires user sign-in, user management, or secure data access using aut... |
| [`firebase_basics`](.agents/skills/firebase_basics/SKILL.md) | Provides foundational Firebase CLI setup, CLI installation, version checks ('firebase-tools@latest --version'), CLI login (including --no-localhost), project crea... |
| [`firebase_crashlytics`](.agents/skills/firebase_crashlytics/SKILL.md) | Comprehensive guide for Firebase Crashlytics, including provisioning and SDK usage. Use this skill when the user needs help setting up Crashlytics, adding crash r... |
| [`firebase_data_connect_basics`](.agents/skills/firebase_data_connect_basics/SKILL.md) | Builds and deploys Firebase SQL Connect (aka Firebase Data Connect) backends with PostgreSQL securely. Use when designing schemas with tables and relations, writi... |
| [`firebase_firestore`](.agents/skills/firebase_firestore/SKILL.md) | Sets up, manages, queries, and configures Cloud Firestore databases (Standard/Enterprise edition), including data modeling, security rules, indexes, and SDK integ... |
| [`firebase_hosting_basics`](.agents/skills/firebase_hosting_basics/SKILL.md) | Deploys and configures classic Firebase Hosting for static websites, single-page apps (SPAs), and microservices. Use when deploying static sites/SPAs, setting up... |
| [`firebase_remote_config_basics`](.agents/skills/firebase_remote_config_basics/SKILL.md) | Manages Firebase Remote Config templates, feature flags, loading strategies, and SDKs (Android, iOS). Use when downloading/deploying remoteconfig JSON templates,... |
| [`firebase_security_rules_auditor`](.agents/skills/firebase_security_rules_auditor/SKILL.md) | Audits Firebase (Firestore, Cloud Storage) security rules for vulnerabilities, privilege escalation, role bypasses, create vs update inconsistencies, resource exh... |
| [`firestore_rules_creation`](.agents/skills/firestore_rules_creation/SKILL.md) | Designs, authors, refactors, and hardens production-grade Cloud Firestore Security Rules (firestore.rules). IMPORTANT: If subagent delegation AND the firestore-ru... |

### 9. Clean-Room Product Replication & Reverse Engineering

*11 skills*

| Skill | Purpose / When to Use |
|---|---|
| [`replica-architect`](.agents/skills/replica-architect/SKILL.md) | Plans the stack, database schema and API for an app clone, from the recon map replica-recon wrote. Picks boring, managed tech, turns the inferred data model into... |
| [`replica-backend`](.agents/skills/replica-backend/SKILL.md) | Builds the backend of an app clone: auth, database migrations and access rules, payments with Stripe, email, background jobs and third-party integrations through... |
| [`replica-brand`](.agents/skills/replica-brand/SKILL.md) | Names and rebrands an app clone so it is the user's own: name candidates with the trademark, domain, store and handle checks to run, a new palette checked for con... |
| [`replica-build`](.agents/skills/replica-build/SKILL.md) | Rebuilds an app screen by screen from the recon map: app shell first, then the core flow as a vertical slice, then every screen with all its states, ticking off t... |
| [`replica-deploy`](.agents/skills/replica-deploy/SKILL.md) | Ships an app clone live on the user's own domain: a preflight gate (tests green, parity must-haves done, rebrand sweep clean, listing linted, legal pages up), pro... |
| [`replica-design`](.agents/skills/replica-design/SKILL.md) | Rebuilds an app's design system for a clone: colour roles, type scale, spacing, radius, shadows and every component with its states, as design tokens plus compone... |
| [`replica-diff`](.agents/skills/replica-diff/SKILL.md) | Compares an app clone against the original: a feature parity score from the feature matrix (weighted by must, should, could) with the missing list in build order,... |
| [`replica-entrepreneur`](.agents/skills/replica-entrepreneur/SKILL.md) | Researches the app being cloned and reads what its real users say in public reviews (App Store, Google Play, G2, Capterra, Trustpilot, Reddit, Hacker News, its ow... |
| [`replica-launch`](.agents/skills/replica-launch/SKILL.md) | Writes the launch for an app clone: the landing page built on the positioning angle, pricing set against the original's public pricing and its users' complaints,... |
| [`replica-recon`](.agents/skills/replica-recon/SKILL.md) | Reverse-engineers any app into a recon map: screen inventory, user flows, component list, inferred data model and a feature matrix, from public pages, screenshots... |
| [`replica-test`](.agents/skills/replica-test/SKILL.md) | Clicks through every flow of an app clone and tests it for bugs: a test plan generated from the recon flows with happy paths and edge cases, Playwright end-to-end... |

### 10. Cybersecurity, AppSec Pentesting & Threat Response

*39 skills*

| Skill | Purpose / When to Use |
|---|---|
| [`ai-security`](.agents/skills/ai-security/SKILL.md) | Use when assessing AI/ML systems for prompt injection, jailbreak vulnerabilities, model inversion risk, data poisoning exposure, or agent tool abuse. Covers MITRE... |
| [`analyzing-web-server-logs-for-intrusion`](.agents/skills/analyzing-web-server-logs-for-intrusion/SKILL.md) | Parse Apache and Nginx access logs to detect SQL injection attempts, local file inclusion, directory traversal, web scanner fingerprints, and brute-force patterns... |
| [`claude-red`](.agents/skills/claude-red/SKILL.md) | Red teaming and offensive security assessment framework based on SnailSploit/claude-red. Use when conducting authorized penetration testing, attack surface mappin... |
| [`conducting-api-security-testing`](.agents/skills/conducting-api-security-testing/SKILL.md) | Conducts security testing of REST, GraphQL, and gRPC APIs to identify vulnerabilities in authentication, authorization, rate limiting, input validation, and busin... |
| [`conducting-external-reconnaissance-with-osint`](.agents/skills/conducting-external-reconnaissance-with-osint/SKILL.md) | Conduct external recon using OSINT techniques to map an organization's external attack surface without touching target systems, gathering DNS records, certificate... |
| [`dependency-auditor`](.agents/skills/dependency-auditor/SKILL.md) | Audit and manage dependencies across multi-language projects. Identifies vulnerabilities, license conflicts, transitive dependency risks, and safe-upgrade paths.... |
| [`exploiting-broken-function-level-authorization`](.agents/skills/exploiting-broken-function-level-authorization/SKILL.md) | Tests APIs for Broken Function Level Authorization (OWASP API5:2023) by identifying admin and privileged endpoints, then reaching them with regular-user credentia... |
| [`exploiting-excessive-data-exposure-in-api`](.agents/skills/exploiting-excessive-data-exposure-in-api/SKILL.md) | Tests APIs for excessive data exposure (OWASP API3:2023) by intercepting raw API responses and comparing them against what the UI actually renders, looking for le... |
| [`exploiting-http-request-smuggling`](.agents/skills/exploiting-http-request-smuggling/SKILL.md) | Detects and exploits HTTP request smuggling caused by Content-Length/Transfer-Encoding parsing discrepancies between front-end and back-end servers, using Burp Su... |
| [`exploiting-idor-vulnerabilities`](.agents/skills/exploiting-idor-vulnerabilities/SKILL.md) | Identifies and exploits Insecure Direct Object Reference (IDOR) vulnerabilities by manipulating object identifiers (numeric IDs, UUIDs, slugs) in API requests and... |
| [`exploiting-insecure-deserialization`](.agents/skills/exploiting-insecure-deserialization/SKILL.md) | Identifying and exploiting insecure deserialization vulnerabilities in Java, PHP, Python, and .NET applications to achieve remote code execution during authorized... |
| [`exploiting-jwt-algorithm-confusion-attack`](.agents/skills/exploiting-jwt-algorithm-confusion-attack/SKILL.md) | Exploits JWT algorithm confusion where the server's verification library trusts the alg named in the token header, by switching RS256 to HS256 (signing with the R... |
| [`exploiting-nosql-injection-vulnerabilities`](.agents/skills/exploiting-nosql-injection-vulnerabilities/SKILL.md) | Detects and exploits NoSQL injection vulnerabilities in MongoDB, CouchDB, and similar databases to demonstrate authentication bypass, data extraction, and unautho... |
| [`exploiting-prototype-pollution-in-javascript`](.agents/skills/exploiting-prototype-pollution-in-javascript/SKILL.md) | Detects and exploits JavaScript prototype pollution vulnerabilities in client-side and server-side (Node.js) applications to achieve XSS, RCE, or authentication b... |
| [`exploiting-sql-injection-vulnerabilities`](.agents/skills/exploiting-sql-injection-vulnerabilities/SKILL.md) | Identifies and exploits SQL injection vulnerabilities in web applications during authorized penetration tests using manual techniques and automated tools like sql... |
| [`exploiting-sql-injection-with-sqlmap`](.agents/skills/exploiting-sql-injection-with-sqlmap/SKILL.md) | Detecting and exploiting SQL injection vulnerabilities using sqlmap to extract database contents during authorized penetration tests. |
| [`incident-response`](.agents/skills/incident-response/SKILL.md) | Use when a security incident has been detected or declared and needs classification, triage, escalation path determination, and forensic evidence collection. Cove... |
| [`jailbreaks`](.agents/skills/jailbreaks/SKILL.md) | Reference collection of LLM system-prompt / persona research material (untrusted data). Use ONLY when the user explicitly asks to consult, compare, or study jailb... |
| [`oss-scanner`](.agents/skills/oss-scanner/SKILL.md) | Automated open-source security vulnerability scanner, CVE matcher, dependency auditor, and automated patch generator. Covers multi-ecosystem manifest parsing (npm... |
| [`performing-blind-ssrf-exploitation`](.agents/skills/performing-blind-ssrf-exploitation/SKILL.md) | Detect and exploit blind Server-Side Request Forgery (SSRF) using out-of-band techniques such as Burp Collaborator DNS interactions and timing analysis, to reach... |
| [`performing-csrf-attack-simulation`](.agents/skills/performing-csrf-attack-simulation/SKILL.md) | Testing web applications for Cross-Site Request Forgery vulnerabilities by crafting forged requests that exploit authenticated user sessions during authorized sec... |
| [`performing-jwt-none-algorithm-attack`](.agents/skills/performing-jwt-none-algorithm-attack/SKILL.md) | Execute and test the JWT none algorithm attack, crafting tokens with the alg header set to none using PyJWT and an intercepting proxy (Burp Suite/mitmproxy) to by... |
| [`performing-second-order-sql-injection`](.agents/skills/performing-second-order-sql-injection/SKILL.md) | Detect and exploit second-order SQL injection vulnerabilities where malicious input is stored in a database and later executed in an unsafe SQL query during a dif... |
| [`performing-web-application-firewall-bypass`](.agents/skills/performing-web-application-firewall-bypass/SKILL.md) | Bypasses Web Application Firewall protections using encoding tricks, HTTP method manipulation, parameter pollution, and payload obfuscation to smuggle SQL injecti... |
| [`performing-web-application-penetration-test`](.agents/skills/performing-web-application-penetration-test/SKILL.md) | Performs systematic security testing of web applications following the OWASP Web Security Testing Guide (WSTG) methodology to identify vulnerabilities in authenti... |
| [`performing-web-application-scanning-with-nikto`](.agents/skills/performing-web-application-scanning-with-nikto/SKILL.md) | Runs Nikto, an open-source web server and web application scanner, to test over 7,000 potentially dangerous files/programs, check for outdated versions across 1,2... |
| [`performing-web-application-vulnerability-triage`](.agents/skills/performing-web-application-vulnerability-triage/SKILL.md) | Triages web application vulnerability findings from DAST/SAST scanners such as Burp Suite and ZAP, using the OWASP Risk Rating Methodology to confirm true positiv... |
| [`performing-web-cache-poisoning-attack`](.agents/skills/performing-web-cache-poisoning-attack/SKILL.md) | Exploiting web cache mechanisms to serve malicious content to other users by poisoning cached responses through unkeyed headers and parameters during authorized s... |
| [`resemble-detect`](.agents/skills/resemble-detect/SKILL.md) | Deepfake detection and media safety — detect AI-generated audio, images, video, and text, trace synthesis sources, analyze media intelligence, and tell people fro... |
| [`scanning-network-with-nmap-advanced`](.agents/skills/scanning-network-with-nmap-advanced/SKILL.md) | Performs advanced network recon using Nmap's Scripting Engine (NSE), timing controls, firewall/IDS evasion, and structured output parsing to discover hosts, enume... |
| [`security-and-hardening`](.agents/skills/security-and-hardening/SKILL.md) | Hardens code against vulnerabilities. Use when auditing an input handler for vulnerabilities, when handling user input, authentication, data storage, or external... |
| [`security-audit`](.agents/skills/security-audit/SKILL.md) | Security guidance and vulnerability review for codebases, APIs, services, CLI tools, libraries, and daemons. Use for security questions, focused reviews, vulnerab... |
| [`skill-security-auditor`](.agents/skills/skill-security-auditor/SKILL.md) | Security audit and vulnerability scanner for AI agent skills before installation. Use when: (1) evaluating a skill from an untrusted source, (2) auditing a skill... |
| [`testing-api-for-broken-object-level-authorization`](.agents/skills/testing-api-for-broken-object-level-authorization/SKILL.md) | Tests REST and GraphQL APIs for Broken Object Level Authorization (BOLA/IDOR, OWASP API1:2023) by intercepting API calls, identifying object ID parameters (numeri... |
| [`testing-api-security-with-owasp-top-10`](.agents/skills/testing-api-security-with-owasp-top-10/SKILL.md) | Systematically assesses REST, GraphQL, and gRPC API endpoints against the OWASP API Security Top 10 (2023) using Burp Suite and Postman for automated and manual t... |
| [`testing-for-xss-vulnerabilities`](.agents/skills/testing-for-xss-vulnerabilities/SKILL.md) | Tests web applications for reflected, stored, and DOM-based Cross-Site Scripting by injecting JavaScript payloads with Burp Suite (XSS extensions, Active Scan++)... |
| [`testing-for-xss-vulnerabilities-with-burpsuite`](.agents/skills/testing-for-xss-vulnerabilities-with-burpsuite/SKILL.md) | Identifying and validating cross-site scripting vulnerabilities using Burp Suite's scanner, intruder, and repeater tools during authorized security assessments. |
| [`testing-for-xxe-injection-vulnerabilities`](.agents/skills/testing-for-xxe-injection-vulnerabilities/SKILL.md) | Discovering and exploiting XML External Entity injection vulnerabilities to read server files, perform SSRF, and exfiltrate data during authorized penetration tests. |
| [`threat-detection`](.agents/skills/threat-detection/SKILL.md) | Use when hunting for threats in an environment, analyzing IOCs, or detecting behavioral anomalies in telemetry. Covers hypothesis-driven threat hunting, IOC sweep... |

### 11. Data Engineering, BigQuery, SQL Migration & Vertex AI

*41 skills*

| Skill | Purpose / When to Use |
|---|---|
| [`accidental-data-loss-prevention`](.agents/skills/accidental-data-loss-prevention/SKILL.md) | **STOP AND VERIFY**: Before running any command or tool that results in irreversible data loss, you MUST obtain explicit user consent. When in doubt, ask. It is b... |
| [`bigquery-ai-ml`](.agents/skills/bigquery-ai-ml/SKILL.md) | Leverages BigQuery's built-in machine learning and GenAI capabilities for advanced data analytics. Use when you need to write SQL queries that perform time-series... |
| [`bigquery-bigframes`](.agents/skills/bigquery-bigframes/SKILL.md) | Generates Python code using BigQuery DataFrames (BigFrames). Use by default for any Python data task involving BigQuery, including data processing, analysis, and... |
| [`bigquery-data-transfer-service`](.agents/skills/bigquery-data-transfer-service/SKILL.md) | Discovers and inspects BigQuery Data Transfer Service (DTS) configurations. Use this to identify existing ingestion pipelines and extract datasource or transfer c... |
| [`bigquery-graph-author`](.agents/skills/bigquery-graph-author/SKILL.md) | Provides an end-to-end journey for authoring a BigQuery property graph from your tables or from a model document/diagram (an ER diagram, an ontology, a semantic m... |
| [`bigquery-graph-query`](.agents/skills/bigquery-graph-query/SKILL.md) | Provides guidelines and best practices for querying BigQuery property graphs and semantic graphs: native GQL (Graph Query Language) pattern matching, multi-hop an... |
| [`bigquery-observability`](.agents/skills/bigquery-observability/SKILL.md) | Provides data-retrieval best practices, tool selection guidance, and performant SQL query syntax for BigQuery telemetry across INFORMATION_SCHEMA, Cloud Monitorin... |
| [`bigquery-optimization`](.agents/skills/bigquery-optimization/SKILL.md) | Provides workflows to optimize BigQuery environments (capacity planning, editions), storage assets (partitioning, clustering, storage lifecycles, billing models),... |
| [`bigquery-troubleshooting`](.agents/skills/bigquery-troubleshooting/SKILL.md) | Provides diagnostic workflows and step-by-step root-cause analysis procedures for actively broken, failing, or slow BigQuery jobs, execution graph and query plan... |
| [`bigtable-basics`](.agents/skills/bigtable-basics/SKILL.md) | Provisions instances and tables, designs performant schemas, and queries data in Bigtable. Use when designing Bigtable row keys, configuring column families, writ... |
| [`building-data-apps`](.agents/skills/building-data-apps/SKILL.md) | Build modern data apps, dashboards, and interactive reports using either React + Vite or Streamlit. Includes optional Gemini Data Analytics chat integration for a... |
| [`cloud-databases-onboarding`](.agents/skills/cloud-databases-onboarding/SKILL.md) | Guides users through discovering their database requirements, recommends a Google Cloud database product or migration destination based on a recommendation matrix... |
| [`curate-context`](.agents/skills/curate-context/SKILL.md) | Creates, imports, pulls, edits, repairs, or publishes a Knowledge Catalog (KC) context set as Open Knowledge Format (OKF v0.2) markdown under 'bundle/' with 'kcmd... |
| [`dak-setup`](.agents/skills/dak-setup/SKILL.md) | Configures (or reconfigures) the Google Cloud Data Agent Kit (DAK) plugin by checking gcloud and ADC credentials, collecting the GCP project ID, region, and servi... |
| [`data-autocleaning`](.agents/skills/data-autocleaning/SKILL.md) | Automated data quality and transformation capabilities for Dataform/dbt/BigQuery pipelines. Processes data sourced from BigQuery or Cloud Storage (GCS), applying... |
| [`dataform-bigquery`](.agents/skills/dataform-bigquery/SKILL.md) | Expertise in generating clean, correct, and efficient Dataform pipeline code for BigQuery ELT. Use this when creating or modifying Dataform pipelines, actions, or... |
| [`dbt-bigquery`](.agents/skills/dbt-bigquery/SKILL.md) | Expert guidance for creating, modifying, and optimizing dbt pipelines for BigQuery. Use this skill whenever user asks for generating or modifying a dbt model or p... |
| [`discover-assets`](.agents/skills/discover-assets/SKILL.md) | Finds and inspects data assets within Google Cloud. Use for any question that needs to discover data sources or find/inspect schemas, metadata, or domain rules fo... |
| [`enforcing-resource-attribution`](.agents/skills/enforcing-resource-attribution/SKILL.md) | Enforces resource attribution for CLI commands. Use this skill whenever you are running 'bq' or 'gcloud' commands via 'run_command'. It ensures mandatory labeling... |
| [`federate-lakehouse-catalog`](.agents/skills/federate-lakehouse-catalog/SKILL.md) | Sets up Google Cloud Lakehouse federated catalogs to remote Iceberg REST Catalogs. Currently supported catalogs: Databricks Unity, AWS Glue. Supported clouds host... |
| [`gcp-composer-troubleshooting`](.agents/skills/gcp-composer-troubleshooting/SKILL.md) | Provides expert guidance for troubleshooting Cloud Composer (Apache Airflow) and Orchestration pipelines. Use this skill when the user asks to generate Root Cause... |
| [`gcp-data-pipelines`](.agents/skills/gcp-data-pipelines/SKILL.md) | Primary entry point for building, managing, and orchestrating data pipelines on Google Cloud. Guides users to the appropriate skill for dbt, Dataflow (Apache Beam... |
| [`gcp-dataflow`](.agents/skills/gcp-dataflow/SKILL.md) | Guides writing, packaging, executing, and troubleshooting Apache Beam pipelines on Dataflow. Use when creating new pipelines, configuring Flex Templates, or analy... |
| [`gcp-managed-airflow-dag-authoring`](.agents/skills/gcp-managed-airflow-dag-authoring/SKILL.md) | Guides the authoring and validation of Apache Airflow DAGs for Managed Service for Apache Airflow (MSAA; formerly Cloud Composer). Covers environment context disc... |
| [`gcp-managed-airflow-migrations`](.agents/skills/gcp-managed-airflow-migrations/SKILL.md) | Provides guidance for migrating Apache Airflow DAGs in Managed Service for Apache Airflow (MSAA; formerly Cloud Composer). Covers migration to Airflow 2.11.1 (MSA... |
| [`gcp-managed-airflow-recommendations`](.agents/skills/gcp-managed-airflow-recommendations/SKILL.md) | Provides recommendations and best practices for creating, configuring, tuning and optimizing Managed Service for Apache Airflow (MSAA, Cloud Composer) environment... |
| [`gcp-managed-spark-upgrades`](.agents/skills/gcp-managed-spark-upgrades/SKILL.md) | Upgrades Spark workloads on Google Cloud Managed Service for Apache Spark (formerly known as Dataproc) clusters and Serverless to a newer image or runtime version... |
| [`gcp-pipeline-orchestration`](.agents/skills/gcp-pipeline-orchestration/SKILL.md) | This skill helps the agent generate or update orchestration pipeline definitions for Google Cloud Composer to initialize orchestration pipeline or update the orch... |
| [`gcp-pipeline-resource-provisioning`](.agents/skills/gcp-pipeline-resource-provisioning/SKILL.md) | Automates declarative resource creation and provisioning for data pipelines, supporting BigQuery, Dataform, Dataproc, BigQuery Data Transfer Service (DTS), and ot... |
| [`gcp-spark`](.agents/skills/gcp-spark/SKILL.md) | Authors, optimizes, and runs PySpark and Spark code on Google Cloud Managed Spark (Dataproc Serverless, clusters, and Spark Connect). Use when: - Authoring or run... |
| [`gcp-spark-observability`](.agents/skills/gcp-spark-observability/SKILL.md) | Monitors, inventories, and assesses Google Cloud Managed Service for Apache Spark (Dataproc Serverless and Dataproc on Compute Engine) environments, clusters, bat... |
| [`gcp-spark-troubleshooting`](.agents/skills/gcp-spark-troubleshooting/SKILL.md) | Provides expert guidance for troubleshooting Google Cloud Spark and Dataproc workloads (Dataproc Serverless batches, interactive sessions, and standard Dataproc c... |
| [`gcs-security-assessment`](.agents/skills/gcs-security-assessment/SKILL.md) | Assesses the security posture of Google Cloud Storage (GCS) buckets and projects. Grounds every finding in gathered telemetry, evaluates buckets against Google se... |
| [`google-cloud-storage-basics`](.agents/skills/google-cloud-storage-basics/SKILL.md) | Stores, retrieves, and manages data as objects in Cloud Storage on Google Cloud (also known colloquially as GCS) buckets. Use when you need to interact with Cloud... |
| [`google-cloud-storage-bucket-architect`](.agents/skills/google-cloud-storage-bucket-architect/SKILL.md) | Creates Cloud Storage (Google Cloud Storage, or GCS) buckets. Analyzes the workload (sensitive data, media hosting, ingestion, web hosting, archiving, backup, log... |
| [`google-cloud-storage-fuse`](.agents/skills/google-cloud-storage-fuse/SKILL.md) | Mounts Cloud Storage buckets as a POSIX file system with Cloud Storage FUSE (gcsfuse). Use when you need to interact with gcsfuse — decide whether FUSE, native gs... |
| [`managing-python-dependencies`](.agents/skills/managing-python-dependencies/SKILL.md) | Ensures proper Python dependency management, avoiding global 'pip install' and adhering to project-specific tooling. Use this skill if any of the following are tr... |
| [`ml-best-practices`](.agents/skills/ml-best-practices/SKILL.md) | CRITICAL RULE: You MUST use this skill whenever the task involves any machine learning tasks or data analysis. Use this skill if the user's prompt or requirements... |
| [`notebook-guidance`](.agents/skills/notebook-guidance/SKILL.md) | This skill guides the use of Jupyter notebooks for data analysis, exploration, and visualization, particularly with BigQuery. It outlines best practices for noteb... |
| [`resolving-mcp-region-configs`](.agents/skills/resolving-mcp-region-configs/SKILL.md) | Mandatory Step 0 pre-flight check for regional Google Cloud MCP servers (Composer dak-composer, Dataform dak-dataform, and Dataflow dak-dataflow) before using reg... |
| [`schema-mapping`](.agents/skills/schema-mapping/SKILL.md) | Guides the process of analyzing, mapping, and documenting transformations between source and target schemas for any database, data warehouse, or data platform. Fo... |

### 12. Bioinformatics, Drug Discovery & Scientific Literature

*51 skills*

| Skill | Purpose / When to Use |
|---|---|
| [`alphafold_database_fetch_and_analyze`](.agents/skills/alphafold_database_fetch_and_analyze/SKILL.md) | Retrieve and analyze AlphaFold predicted structures for a protein. Use when the user provides a specific UniProt Accession ID and wants structural confidence metr... |
| [`alphagenome_atlas_website_links`](.agents/skills/alphagenome_atlas_website_links/SKILL.md) | Constructs deep-links and URLs for the AlphaGenome Atlas website. Supports generating single-variant exploration links (1-based VCF-style coordinates), genomic lo... |
| [`alphagenome_single_variant_analysis`](.agents/skills/alphagenome_single_variant_analysis/SKILL.md) | Analyzes genetic variant effects on gene expression (RNA-seq), chromatin accessibility (DNASE), histone marks (ChIP), and transcription factors using the AlphaGen... |
| [`alphagenome_variant_impact_score`](.agents/skills/alphagenome_variant_impact_score/SKILL.md) | Score, annotate, and analyze the functional impact of genetic variants using AlphaGenome Variant Impact (AVI) scores. Query variants in chr:pos:ref>alt format, an... |
| [`biomolecular_structure_viewer`](.agents/skills/biomolecular_structure_viewer/SKILL.md) | Interactive 3D biomolecular structure viewer via Mol*. Renders 3D molecular structures from local workspace files (.cif, .mmcif, .pdb) or conversation artifacts,... |
| [`chembl_database`](.agents/skills/chembl_database/SKILL.md) | Query the ChEMBL database for bioactive molecules, drug targets, bioactivity data, approved drugs, and chemical structures. Use when the user asks about compounds... |
| [`cheminformatics_cofolding`](.agents/skills/cheminformatics_cofolding/SKILL.md) | Co-folds protein-ligand, protein-DNA/RNA, and covalent inhibitor complexes: prepares AlphaFold 3 JSON, Boltz-2 YAML, and Boltz API (boltz-2.1) inputs, extracts bo... |
| [`cheminformatics_core`](.agents/skills/cheminformatics_core/SKILL.md) | Computes RDKit physicochemical descriptors (MW, cLogP, TPSA, CNS MPO, SA score), PAINS/Brenk structural alerts, pH 7.4 ionization, congeneric series curation, act... |
| [`cheminformatics_doc2mol`](.agents/skills/cheminformatics_doc2mol/SKILL.md) | Extracts and curates validated chemical structures from patents, literature, synthesis procedures, and Markush core/R-group tables: resolves IUPAC names via OPSIN... |
| [`cheminformatics_ml`](.agents/skills/cheminformatics_ml/SKILL.md) | Trains, benchmarks, and evaluates predictive SAR and QSAR/ADMET models for chemical series: small-N regularized regressors, nested cross-validation, Tukey HSD mod... |
| [`cheminformatics_physics`](.agents/skills/cheminformatics_physics/SKILL.md) | Simulates 3D molecular physics, conformer ensembles, and CADD workflows: pH-dependent ligand and receptor protonation, ETKDGv3 3D conformer generation, dihedral/r... |
| [`cheminformatics_reactions`](.agents/skills/cheminformatics_reactions/SKILL.md) | Proposes and models organic reactions, retrosynthesis, multi-step synthesis routes, intramolecular cyclizations, and reaction SMARTS: checks experimental preceden... |
| [`clinical_trials_database`](.agents/skills/clinical_trials_database/SKILL.md) | Query ClinicalTrials.gov via APIv2. Use when you want to search for trials by condition, drug, location, status, or phase; retrieve trial details by NCT ID; check... |
| [`clinvar_database`](.agents/skills/clinvar_database/SKILL.md) | Use when needing clinical significance, pathogenicity classifications (e.g., Pathogenic, Benign, VUS), clinical evidence rationales, or finding "hard positive" be... |
| [`credentials`](.agents/skills/credentials/SKILL.md) | Instructions for handling API keys and credentials safely, verifying their presence, and prompting the user to add them if missing using a safe protocol. |
| [`dbsnp_database`](.agents/skills/dbsnp_database/SKILL.md) | Use when you want to look up, map, and search for short genetic variants (SNPs, indels) in NCBI's dbSNP database. Resolves between rsIDs, genomic coordinates in V... |
| [`deep-research`](.agents/skills/deep-research/SKILL.md) | Conduct in-depth research across multiple sources and synthesize findings into clear, readable reports. Use when the user requests in-depth or comprehensive resea... |
| [`embl_ebi_ols`](.agents/skills/embl_ebi_ols/SKILL.md) | Query and search the EMBL-EBI Ontology Lookup Service (OLS) for biomedical ontology terms, definitions, and hierarchies across 250+ ontologies (e.g., GO, DOID, HP... |
| [`encode_ccres_database`](.agents/skills/encode_ccres_database/SKILL.md) | Query the ENCODE Registry of cis-Regulatory Elements (cCREs) via the SCREEN GraphQL API, or make custom queries to the ENCODE Portal REST API for experiments and... |
| [`ensembl_database`](.agents/skills/ensembl_database/SKILL.md) | Query the Ensembl database to resolve gene, transcript, and protein IDs, fetch genomic or protein sequences, retrieve gene structures (exons), and get variant con... |
| [`foldseek_structural_search`](.agents/skills/foldseek_structural_search/SKILL.md) | Performs 3D structural searches of proteins against various databases (PDB, AlphaFold, CATH, MGnify, etc.) using the Foldseek API. Use ONLY when the user provides... |
| [`gnomad_database`](.agents/skills/gnomad_database/SKILL.md) | Query the Genome Aggregation Database (gnomAD). Use when determining the rarity or allele frequency of specific genetic variants, retrieving gene constraint metri... |
| [`gtex_database`](.agents/skills/gtex_database/SKILL.md) | Use when you want to retrieve quantitative RNA expression data and variant eQTL information from the GTEx (Genotype-Tissue Expression) Project across 54 non-disea... |
| [`human_protein_atlas_database`](.agents/skills/human_protein_atlas_database/SKILL.md) | Use when you want to retrieve semi-quantitative protein expression and spatial localisation data from the Human Protein Atlas (HPA). |
| [`interpro_database`](.agents/skills/interpro_database/SKILL.md) | Identify domains, families, and sites in proteins; find all proteins in a family or sharing a domain; explore species distribution for a domain; annotate genomes... |
| [`jaspar_database`](.agents/skills/jaspar_database/SKILL.md) | Query the JASPAR database for Transcription Factor (TF) binding profiles. Use when retrieving Position Frequency Matrices (PFMs) or Position Weight Matrices (PWMs... |
| [`literature_search_arxiv`](.agents/skills/literature_search_arxiv/SKILL.md) | Search for scientific papers, preprints, and publications on arXiv. Extract metadata, abstracts, and download full-text PDFs or HTML versions of papers. Use when... |
| [`literature_search_biorxiv`](.agents/skills/literature_search_biorxiv/SKILL.md) | Browse, filter, and download life sciences, biology, and medical preprints from bioRxiv and medRxiv. Supports fetching paper metadata by DOI, and browsing by date... |
| [`literature_search_europepmc`](.agents/skills/literature_search_europepmc/SKILL.md) | Search Europe PMC for scientific literature and download open-access full texts and PDFs. Retrieve full-text XML/plain text by PMCID, get citation lists and bibli... |
| [`literature_search_openalex`](.agents/skills/literature_search_openalex/SKILL.md) | Query the OpenAlex scholarly database for research papers, authors, institutions, topics, sources, publishers, funders, geo-locations, and keywords. Use when sear... |
| [`market-research`](.agents/skills/market-research/SKILL.md) | Use when doing upstream market-research methodology — sizing a market as TAM/SAM/SOM computed BOTH top-down and bottoms-up (never a single unsourced number), plan... |
| [`ncbi_sequence_fetch`](.agents/skills/ncbi_sequence_fetch/SKILL.md) | Retrieve protein and nucleotide sequences from NCBI databases using E-utilities. Supports direct accession lookup, CDS translation, gene+organism search, locus lo... |
| [`openfda_database`](.agents/skills/openfda_database/SKILL.md) | Query, search, and download data from the openFDA API for drugs, devices, foods, tobacco, cosmetics, animal and veterinary products, substances, and transparency... |
| [`opentargets_database`](.agents/skills/opentargets_database/SKILL.md) | Query Open Targets Platform for target-disease associations, drug target discovery, tractability/safety data, genetics/omics evidence, known drugs, for therapeuti... |
| [`pdb_database`](.agents/skills/pdb_database/SKILL.md) | Use when you want to search for or download experimentally-determined 3D structures for biomolecules (proteins, nucleic acids, bound ligands). Supports searching... |
| [`predictingthepast`](.agents/skills/predictingthepast/SKILL.md) | Ancient text restoration, attribution, dating, contextualization, and embedding via Aeneas (Latin) / Ithaca (Ancient Greek). Use when asked to "restore", "attribu... |
| [`product-research`](.agents/skills/product-research/SKILL.md) | Use when planning and synthesizing product/user research as a method-and-repository discipline — selecting the right method for the goal (generative interviews vs... |
| [`protein_sequence_msa`](.agents/skills/protein_sequence_msa/SKILL.md) | Performs multiple sequence alignment of proteins with EBI Clustal Omega. Use when you need to align multiple sequences to assess similarity, domain conservation,... |
| [`protein_sequence_similarity_search`](.agents/skills/protein_sequence_similarity_search/SKILL.md) | Searches for homologous protein sequences using MMseqs2 (fast, default) or BLAST (comprehensive, fallback). Trigger this whenever the user provides a protein sequ... |
| [`pubchem_database`](.agents/skills/pubchem_database/SKILL.md) | Query PubChem, search by name/CID/SMILES, retrieve properties, similarity/substructure searches, bioactivity, for cheminformatics. Use when a user asks about a sp... |
| [`pubmed_database`](.agents/skills/pubmed_database/SKILL.md) | Search PubMed for scientific literature, including published clinical trials. Fetch abstracts and full text. Link published research to biological databases (gene... |
| [`pymol`](.agents/skills/pymol/SKILL.md) | Visualize, analyze, and render protein and molecular structures using PyMOL. Use when the user wants to create images of protein structures, perform structural al... |
| [`quickgo_database`](.agents/skills/quickgo_database/SKILL.md) | Query the QuickGO and Evidence & Conclusion Ontology (ECO) REST API. Use this when you need to map genes to biological processes, molecular functions, or cellular... |
| [`rdkit_general`](.agents/skills/rdkit_general/SKILL.md) | Generates 2D chemical structure depictions (PNG/SVG), interactive HTML compound grids, standalone chemical applications/visualizers, and ChemDraw (.cdxml/.cdx) do... |
| [`reactome_database`](.agents/skills/reactome_database/SKILL.md) | Query the Reactome database (Analysis and Content Services). Use when the user asks about pathway analysis, gene list enrichment, retrieving results by token, fin... |
| [`string_database`](.agents/skills/string_database/SKILL.md) | Query the STRING database for protein-protein interactions (PPIs), functional enrichment, and homology. Use when the user asks about interactions between specific... |
| [`ucsc_conservation_and_tfbs`](.agents/skills/ucsc_conservation_and_tfbs/SKILL.md) | Fetch Evolutionary Conservation scores (phyloP, phastCons) and Transcription Factor Binding Sites (TFBS) from the UCSC Genome Browser. Use when analyzing whether... |
| [`unibind_database`](.agents/skills/unibind_database/SKILL.md) | Queries the UniBind database for experimentally validated transcription factor (TF) binding sites. Use when retrieving direct TF-DNA interaction datasets, downloa... |
| [`uniprot_database`](.agents/skills/uniprot_database/SKILL.md) | Access protein metadata, function, taxonomy, and sequences across UniProtKB, UniParc, and UniRef. Use when searching for proteins, mapping identifiers, or retriev... |
| [`uv`](.agents/skills/uv/SKILL.md) | Checks whether the uv Python package manager is installed and installs it if missing. Ensures uv is on PATH. Use when another skill requires uv as a prerequisite. |
| [`workflow_skill_creator`](.agents/skills/workflow_skill_creator/SKILL.md) | Distills a completed user workflow or interaction into a reusable agent skill. Use when the user asks to turn their workflow, interaction, or multi-step process i... |

### 13. Multimodal Vision, Video Intelligence & Audio Pipelines

*8 skills*

| Skill | Purpose / When to Use |
|---|---|
| [`asking-with-evidence`](.agents/skills/asking-with-evidence/SKILL.md) | The user asks a question about a video that was already watched or indexed — "what did they say about X", "what error code appears", "what happens at 2:30", "does... |
| [`configuring-vision`](.agents/skills/configuring-vision/SKILL.md) | The user wants to connect an LLM or vision provider, already has an API key, asks "can I use OpenAI/Anthropic/Gemini/OpenRouter", wants local Ollama, or needs dif... |
| [`extracting-structure`](.agents/skills/extracting-structure/SKILL.md) | The user wants structure pulled out of a watched video — "make chapters for this video", "where does the bug appear in this recording", "turn this screen recordin... |
| [`the-loop`](.agents/skills/the-loop/SKILL.md) | The user built or changed something visual — a UI, an animation, a game, a generated video — and wants it verified, or asks "why does my UI look wrong", "check th... |
| [`video-memory`](.agents/skills/video-memory/SKILL.md) | The user asks about videos watched in the past or across sessions — "have we watched anything about X", "which video showed that error", "what did that meeting de... |
| [`watch`](.agents/skills/watch/SKILL.md) | Watch any video (URL, stream, or local path) via Watch Skill. Downloads, extracts scene-aware deduped frames, OCRs them, transcribes (captions first, then local W... |
| [`watching-videos`](.agents/skills/watching-videos/SKILL.md) | The user shared a video URL, a YouTube/TikTok/stream link, a local video file, a screen recording, a meeting recording, or a playlist/folder of videos — "watch th... |
| [`youtube-video-research`](.agents/skills/youtube-video-research/SKILL.md) | Enhance any deep research task with first-hand YouTube video evidence via manus-analyze-video. Highly recommended whenever the task involves deep research, invest... |

### 14. Content, LinkedIn Growth, Slides & Document Tooling

*30 skills*

| Skill | Purpose / When to Use |
|---|---|
| [`banner-design`](.agents/skills/banner-design/SKILL.md) | Design banners for social media, ads, website heroes, creative assets, and print. Multiple art direction options with optional generated or supplied visuals. Acti... |
| [`brand`](.agents/skills/brand/SKILL.md) | Brand voice, visual identity, messaging frameworks, asset management, brand consistency. Activate for branded content, tone of voice, marketing assets, brand comp... |
| [`brandkit`](.agents/skills/brandkit/SKILL.md) | Moved to github.com/Leonxlnx/imagegen-skills. Runs only when called by name. |
| [`cognitive-doc-design`](.agents/skills/cognitive-doc-design/SKILL.md) | Design docs that reduce cognitive load. Trigger: writing guides, READMEs, RFCs, onboarding, architecture, or review-facing docs. |
| [`comment-writer`](.agents/skills/comment-writer/SKILL.md) | Write warm, direct collaboration comments. Trigger: PR feedback, issue replies, reviews, Slack messages, or GitHub comments. |
| [`documentation-and-adrs`](.agents/skills/documentation-and-adrs/SKILL.md) | Records decisions and documentation. Use when you need to document an architecture decision (ADR) or the reasoning behind a design choice, when changing public AP... |
| [`docx`](.agents/skills/docx/SKILL.md) | Comprehensive document creation, editing, and analysis with support for tracked changes, comments, formatting preservation, and text extraction. When Claude needs... |
| [`ebook-treasure-chest`](.agents/skills/ebook-treasure-chest/SKILL.md) | Production-grade digital library and academic repository management. Covers dual-server deployment (Calibre-web and Kavita), OPDS feed configuration for e-readers... |
| [`humanizer`](.agents/skills/humanizer/SKILL.md) | Rewrite AI-sounding text so it reads like the writer without changing what it says. Use when editing or reviewing prose for AI tells: not-X-but-Y contrasts, one-l... |
| [`linkedin-comment-drafter`](.agents/skills/linkedin-comment-drafter/SKILL.md) | Draft a LinkedIn comment on someone else's post from its URL, or reshare (repost) it to your feed with optional commentary. Use when the user pastes a post URL an... |
| [`linkedin-content-planner`](.agents/skills/linkedin-content-planner/SKILL.md) | Generate a 7-day LinkedIn content plan from a theme, audience, and pillars. Produces per-day post pillar, format, hook type, CTA, posting time, daily comment targ... |
| [`linkedin-employee-advocacy`](.agents/skills/linkedin-employee-advocacy/SKILL.md) | Stand up and run a LinkedIn employee advocacy program for a marketing or sales team. Covers 14-day launch playbook, brand-guideline governance, per-post time budg... |
| [`linkedin-engager-analytics`](.agents/skills/linkedin-engager-analytics/SKILL.md) | Pull the people who liked or commented on any LinkedIn post and segment them by ICP fit (peer / aspirational / prospect / other). Produces an engager roster, tier... |
| [`linkedin-hook-extractor`](.agents/skills/linkedin-hook-extractor/SKILL.md) | Reverse-engineer the hook formula from a viral LinkedIn post URL. Returns which of the 20 canonical 2026 formulas it uses (anaphora, R.I.P., year-pivot, time-anch... |
| [`linkedin-humanizer`](.agents/skills/linkedin-humanizer/SKILL.md) | Remove AI tells from LinkedIn posts/comments: 2026 vocabulary density, reveal bridges, staccato fragments, stacked triads, performed sincerity. Tiered rewriter pl... |
| [`linkedin-interviewer`](.agents/skills/linkedin-interviewer/SKILL.md) | Interview the user for the raw material their posts are made of. Builds a lasting Story Bank of roles, numbers, turning points, scars and positions, or runs a foc... |
| [`linkedin-post-writer`](.agents/skills/linkedin-post-writer/SKILL.md) | Draft a new LinkedIn post from scratch using one of 20 2026 hook formulas (anaphora, R.I.P., time-anchor, curiosity-gap, contrarian, controlled A/B, false-binary,... |
| [`linkedin-profile-optimizer`](.agents/skills/linkedin-profile-optimizer/SKILL.md) | Audit and rewrite a LinkedIn profile end-to-end for 2026: headline, About 7-step, Featured, banner, photo, Experience metrics, Skills, custom URL, recommendations... |
| [`linkedin-reply-handler`](.agents/skills/linkedin-reply-handler/SKILL.md) | Draft a reply to one LinkedIn comment from its URL, or sweep a whole thread from just the post URL and draft a reply to every comment worth answering, in one batc... |
| [`linkedin-repurposer`](.agents/skills/linkedin-repurposer/SKILL.md) | Repurpose existing content into a native LinkedIn post. Take a tweet, thread, YouTube video, blog, or newsletter and rebuild it for LinkedIn: re-hook before the f... |
| [`linkedin-thread-monitor`](.agents/skills/linkedin-thread-monitor/SKILL.md) | Track which of your LinkedIn comments earned author replies. Flags the 6-24h warm-reply window where thread momentum peaks, classifies threads as hot/warm/cool/do... |
| [`pdf`](.agents/skills/pdf/SKILL.md) | Comprehensive PDF manipulation toolkit for extracting text and tables, creating new PDFs, merging/splitting documents, and handling forms. When Claude needs to fi... |
| [`ppt-master`](.agents/skills/ppt-master/SKILL.md) | AI-driven presentation workflow for generating editable PPTX decks and slides, reconstructing page visuals, creating reusable Brand/Style/Layout/Deck workspaces,... |
| [`pptx`](.agents/skills/pptx/SKILL.md) | Presentation creation, editing, and analysis. When Claude needs to work with presentations (.pptx files) for: (1) Creating new presentations, (2) Modifying or edi... |
| [`slides`](.agents/skills/slides/SKILL.md) | Create strategic HTML presentations with Chart.js, design tokens, responsive layouts, copywriting formulas, and contextual slide strategies. |
| [`writing-beats`](.agents/skills/writing-beats/SKILL.md) | Writing, exploit; assemble raw material into a journey of beats, grounding each term before a beat leans on it. |
| [`writing-for-agents`](.agents/skills/writing-for-agents/SKILL.md) | Writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.md. |
| [`writing-fragments`](.agents/skills/writing-fragments/SKILL.md) | Writing, explore: mine raw fragments, no structure yet. |
| [`writing-shape`](.agents/skills/writing-shape/SKILL.md) | Writing, exploit: shape raw material into an article, paragraph by paragraph. |
| [`xlsx`](.agents/skills/xlsx/SKILL.md) | Comprehensive spreadsheet creation, editing, and analysis with support for formulas, formatting, data analysis, and visualization. When Claude needs to work with... |

### 15. Google Workspace Automation (`gws`), Recipes & Personas

*95 skills*

| Skill | Purpose / When to Use |
|---|---|
| [`gws-admin-reports`](.agents/skills/gws-admin-reports/SKILL.md) | Google Workspace Admin SDK: Audit logs and usage reports. |
| [`gws-calendar`](.agents/skills/gws-calendar/SKILL.md) | Google Calendar: Manage calendars and events. |
| [`gws-calendar-agenda`](.agents/skills/gws-calendar-agenda/SKILL.md) | Google Calendar: Show upcoming events across all calendars. |
| [`gws-calendar-insert`](.agents/skills/gws-calendar-insert/SKILL.md) | Google Calendar: Create a new event. |
| [`gws-chat`](.agents/skills/gws-chat/SKILL.md) | Google Chat: Manage Chat spaces and messages. |
| [`gws-chat-send`](.agents/skills/gws-chat-send/SKILL.md) | Google Chat: Send a message to a space. |
| [`gws-classroom`](.agents/skills/gws-classroom/SKILL.md) | Google Classroom: Manage classes, rosters, and coursework. |
| [`gws-docs`](.agents/skills/gws-docs/SKILL.md) | Read and write Google Docs. |
| [`gws-docs-write`](.agents/skills/gws-docs-write/SKILL.md) | Google Docs: Append text to a document. |
| [`gws-drive`](.agents/skills/gws-drive/SKILL.md) | Google Drive: Manage files, folders, and shared drives. |
| [`gws-drive-upload`](.agents/skills/gws-drive-upload/SKILL.md) | Google Drive: Upload a file with automatic metadata. |
| [`gws-events`](.agents/skills/gws-events/SKILL.md) | Subscribe to Google Workspace events. |
| [`gws-events-renew`](.agents/skills/gws-events-renew/SKILL.md) | Google Workspace Events: Renew/reactivate Workspace Events subscriptions. |
| [`gws-events-subscribe`](.agents/skills/gws-events-subscribe/SKILL.md) | Google Workspace Events: Subscribe to Workspace events and stream them as NDJSON. |
| [`gws-forms`](.agents/skills/gws-forms/SKILL.md) | Read and write Google Forms. |
| [`gws-gmail`](.agents/skills/gws-gmail/SKILL.md) | Gmail: Send, read, and manage email. |
| [`gws-gmail-forward`](.agents/skills/gws-gmail-forward/SKILL.md) | Gmail: Forward a message to new recipients. |
| [`gws-gmail-read`](.agents/skills/gws-gmail-read/SKILL.md) | Gmail: Read a message and extract its body or headers. |
| [`gws-gmail-reply`](.agents/skills/gws-gmail-reply/SKILL.md) | Gmail: Reply to a message (handles threading automatically). |
| [`gws-gmail-reply-all`](.agents/skills/gws-gmail-reply-all/SKILL.md) | Gmail: Reply-all to a message (handles threading automatically). |
| [`gws-gmail-send`](.agents/skills/gws-gmail-send/SKILL.md) | Gmail: Send an email. |
| [`gws-gmail-triage`](.agents/skills/gws-gmail-triage/SKILL.md) | Gmail: Show unread inbox summary (sender, subject, date). |
| [`gws-gmail-watch`](.agents/skills/gws-gmail-watch/SKILL.md) | Gmail: Watch for new emails and stream them as NDJSON. |
| [`gws-keep`](.agents/skills/gws-keep/SKILL.md) | Manage Google Keep notes. |
| [`gws-meet`](.agents/skills/gws-meet/SKILL.md) | Manage Google Meet conferences. |
| [`gws-modelarmor`](.agents/skills/gws-modelarmor/SKILL.md) | Google Model Armor: Filter user-generated content for safety. |
| [`gws-modelarmor-create-template`](.agents/skills/gws-modelarmor-create-template/SKILL.md) | Google Model Armor: Create a new Model Armor template. |
| [`gws-modelarmor-sanitize-prompt`](.agents/skills/gws-modelarmor-sanitize-prompt/SKILL.md) | Google Model Armor: Sanitize a user prompt through a Model Armor template. |
| [`gws-modelarmor-sanitize-response`](.agents/skills/gws-modelarmor-sanitize-response/SKILL.md) | Google Model Armor: Sanitize a model response through a Model Armor template. |
| [`gws-people`](.agents/skills/gws-people/SKILL.md) | Google People: Manage contacts and profiles. |
| [`gws-script`](.agents/skills/gws-script/SKILL.md) | Manage Google Apps Script projects. |
| [`gws-script-push`](.agents/skills/gws-script-push/SKILL.md) | Google Apps Script: Upload local files to an Apps Script project. |
| [`gws-shared`](.agents/skills/gws-shared/SKILL.md) | gws CLI: Shared patterns for authentication, global flags, and output formatting. |
| [`gws-sheets`](.agents/skills/gws-sheets/SKILL.md) | Google Sheets: Read and write spreadsheets. |
| [`gws-sheets-append`](.agents/skills/gws-sheets-append/SKILL.md) | Google Sheets: Append a row to a spreadsheet. |
| [`gws-sheets-read`](.agents/skills/gws-sheets-read/SKILL.md) | Google Sheets: Read values from a spreadsheet. |
| [`gws-slides`](.agents/skills/gws-slides/SKILL.md) | Google Slides: Read and write presentations. |
| [`gws-tasks`](.agents/skills/gws-tasks/SKILL.md) | Google Tasks: Manage task lists and tasks. |
| [`gws-workflow`](.agents/skills/gws-workflow/SKILL.md) | Google Workflow: Cross-service productivity workflows. |
| [`gws-workflow-email-to-task`](.agents/skills/gws-workflow-email-to-task/SKILL.md) | Google Workflow: Convert a Gmail message into a Google Tasks entry. |
| [`gws-workflow-file-announce`](.agents/skills/gws-workflow-file-announce/SKILL.md) | Google Workflow: Announce a Drive file in a Chat space. |
| [`gws-workflow-meeting-prep`](.agents/skills/gws-workflow-meeting-prep/SKILL.md) | Google Workflow: Prepare for your next meeting: agenda, attendees, and linked docs. |
| [`gws-workflow-standup-report`](.agents/skills/gws-workflow-standup-report/SKILL.md) | Google Workflow: Today's meetings + open tasks as a standup summary. |
| [`gws-workflow-weekly-digest`](.agents/skills/gws-workflow-weekly-digest/SKILL.md) | Google Workflow: Weekly summary: this week's meetings + unread email count. |
| [`persona-content-creator`](.agents/skills/persona-content-creator/SKILL.md) | Create, organize, and distribute content across Workspace. |
| [`persona-customer-support`](.agents/skills/persona-customer-support/SKILL.md) | Manage customer support — track tickets, respond, escalate issues. |
| [`persona-event-coordinator`](.agents/skills/persona-event-coordinator/SKILL.md) | Plan and manage events — scheduling, invitations, and logistics. |
| [`persona-exec-assistant`](.agents/skills/persona-exec-assistant/SKILL.md) | Manage an executive's schedule, inbox, and communications. |
| [`persona-hr-coordinator`](.agents/skills/persona-hr-coordinator/SKILL.md) | Handle HR workflows — onboarding, announcements, and employee comms. |
| [`persona-it-admin`](.agents/skills/persona-it-admin/SKILL.md) | Administer IT — monitor security and configure Workspace. |
| [`persona-project-manager`](.agents/skills/persona-project-manager/SKILL.md) | Coordinate projects — track tasks, schedule meetings, and share docs. |
| [`persona-researcher`](.agents/skills/persona-researcher/SKILL.md) | Organize research — manage references, notes, and collaboration. |
| [`persona-sales-ops`](.agents/skills/persona-sales-ops/SKILL.md) | Manage sales workflows — track deals, schedule calls, client comms. |
| [`persona-team-lead`](.agents/skills/persona-team-lead/SKILL.md) | Lead a team — run standups, coordinate tasks, and communicate. |
| [`recipe-backup-sheet-as-csv`](.agents/skills/recipe-backup-sheet-as-csv/SKILL.md) | Export a Google Sheets spreadsheet as a CSV file for local backup or processing. |
| [`recipe-batch-invite-to-event`](.agents/skills/recipe-batch-invite-to-event/SKILL.md) | Add a list of attendees to an existing Google Calendar event and send notifications. |
| [`recipe-block-focus-time`](.agents/skills/recipe-block-focus-time/SKILL.md) | Create recurring focus time blocks on Google Calendar to protect deep work hours. |
| [`recipe-bulk-download-folder`](.agents/skills/recipe-bulk-download-folder/SKILL.md) | List and download all files from a Google Drive folder. |
| [`recipe-collect-form-responses`](.agents/skills/recipe-collect-form-responses/SKILL.md) | Retrieve and review responses from a Google Form. |
| [`recipe-compare-sheet-tabs`](.agents/skills/recipe-compare-sheet-tabs/SKILL.md) | Read data from two tabs in a Google Sheet to compare and identify differences. |
| [`recipe-copy-sheet-for-new-month`](.agents/skills/recipe-copy-sheet-for-new-month/SKILL.md) | Duplicate a Google Sheets template tab for a new month of tracking. |
| [`recipe-create-classroom-course`](.agents/skills/recipe-create-classroom-course/SKILL.md) | Create a Google Classroom course and invite students. |
| [`recipe-create-doc-from-template`](.agents/skills/recipe-create-doc-from-template/SKILL.md) | Copy a Google Docs template, fill in content, and share with collaborators. |
| [`recipe-create-events-from-sheet`](.agents/skills/recipe-create-events-from-sheet/SKILL.md) | Read event data from a Google Sheets spreadsheet and create Google Calendar entries for each row. |
| [`recipe-create-expense-tracker`](.agents/skills/recipe-create-expense-tracker/SKILL.md) | Set up a Google Sheets spreadsheet for tracking expenses with headers and initial entries. |
| [`recipe-create-feedback-form`](.agents/skills/recipe-create-feedback-form/SKILL.md) | Create a Google Form for feedback and share it via Gmail. |
| [`recipe-create-gmail-filter`](.agents/skills/recipe-create-gmail-filter/SKILL.md) | Create a Gmail filter to automatically label, star, or categorize incoming messages. |
| [`recipe-create-meet-space`](.agents/skills/recipe-create-meet-space/SKILL.md) | Create a Google Meet meeting space and share the join link. |
| [`recipe-create-presentation`](.agents/skills/recipe-create-presentation/SKILL.md) | Create a new Google Slides presentation and add initial slides. |
| [`recipe-create-shared-drive`](.agents/skills/recipe-create-shared-drive/SKILL.md) | Create a Google Shared Drive and add members with appropriate roles. |
| [`recipe-create-task-list`](.agents/skills/recipe-create-task-list/SKILL.md) | Set up a new Google Tasks list with initial tasks. |
| [`recipe-create-vacation-responder`](.agents/skills/recipe-create-vacation-responder/SKILL.md) | Enable a Gmail out-of-office auto-reply with a custom message and date range. |
| [`recipe-draft-email-from-doc`](.agents/skills/recipe-draft-email-from-doc/SKILL.md) | Read content from a Google Doc and use it as the body of a Gmail message. |
| [`recipe-email-drive-link`](.agents/skills/recipe-email-drive-link/SKILL.md) | Share a Google Drive file and email the link with a message to recipients. |
| [`recipe-find-free-time`](.agents/skills/recipe-find-free-time/SKILL.md) | Query Google Calendar free/busy status for multiple users to find a meeting slot. |
| [`recipe-find-large-files`](.agents/skills/recipe-find-large-files/SKILL.md) | Identify large Google Drive files consuming storage quota. |
| [`recipe-forward-labeled-emails`](.agents/skills/recipe-forward-labeled-emails/SKILL.md) | Find Gmail messages with a specific label and forward them to another address. |
| [`recipe-generate-report-from-sheet`](.agents/skills/recipe-generate-report-from-sheet/SKILL.md) | Read data from a Google Sheet and create a formatted Google Docs report. |
| [`recipe-label-and-archive-emails`](.agents/skills/recipe-label-and-archive-emails/SKILL.md) | Apply Gmail labels to matching messages and archive them to keep your inbox clean. |
| [`recipe-log-deal-update`](.agents/skills/recipe-log-deal-update/SKILL.md) | Append a deal status update to a Google Sheets sales tracking spreadsheet. |
| [`recipe-organize-drive-folder`](.agents/skills/recipe-organize-drive-folder/SKILL.md) | Create a Google Drive folder structure and move files into the right locations. |
| [`recipe-plan-weekly-schedule`](.agents/skills/recipe-plan-weekly-schedule/SKILL.md) | Review your Google Calendar week, identify gaps, and add events to fill them. |
| [`recipe-post-mortem-setup`](.agents/skills/recipe-post-mortem-setup/SKILL.md) | Create a Google Docs post-mortem, schedule a Google Calendar review, and notify via Chat. |
| [`recipe-reschedule-meeting`](.agents/skills/recipe-reschedule-meeting/SKILL.md) | Move a Google Calendar event to a new time and automatically notify all attendees. |
| [`recipe-review-meet-participants`](.agents/skills/recipe-review-meet-participants/SKILL.md) | Review who attended a Google Meet conference and for how long. |
| [`recipe-review-overdue-tasks`](.agents/skills/recipe-review-overdue-tasks/SKILL.md) | Find Google Tasks that are past due and need attention. |
| [`recipe-save-email-attachments`](.agents/skills/recipe-save-email-attachments/SKILL.md) | Find Gmail messages with attachments and save them to a Google Drive folder. |
| [`recipe-save-email-to-doc`](.agents/skills/recipe-save-email-to-doc/SKILL.md) | Save a Gmail message body into a Google Doc for archival or reference. |
| [`recipe-schedule-recurring-event`](.agents/skills/recipe-schedule-recurring-event/SKILL.md) | Create a recurring Google Calendar event with attendees. |
| [`recipe-send-team-announcement`](.agents/skills/recipe-send-team-announcement/SKILL.md) | Send a team announcement via both Gmail and a Google Chat space. |
| [`recipe-share-doc-and-notify`](.agents/skills/recipe-share-doc-and-notify/SKILL.md) | Share a Google Docs document with edit access and email collaborators the link. |
| [`recipe-share-event-materials`](.agents/skills/recipe-share-event-materials/SKILL.md) | Share Google Drive files with all attendees of a Google Calendar event. |
| [`recipe-share-folder-with-team`](.agents/skills/recipe-share-folder-with-team/SKILL.md) | Share a Google Drive folder and all its contents with a list of collaborators. |
| [`recipe-sync-contacts-to-sheet`](.agents/skills/recipe-sync-contacts-to-sheet/SKILL.md) | Export Google Contacts directory to a Google Sheets spreadsheet. |
| [`recipe-watch-drive-changes`](.agents/skills/recipe-watch-drive-changes/SKILL.md) | Subscribe to change notifications on a Google Drive file or folder. |

### 16. Homelab, SSH Servers, Linux Desktop & Self-Hosting

*7 skills*

| Skill | Purpose / When to Use |
|---|---|
| [`claude-homelab`](.agents/skills/claude-homelab/SKILL.md) | Homelab orchestration and MCP server management based on jmagar/claude-homelab. Use when managing, querying, or troubleshooting homelab containers, Proxmox/VMs, H... |
| [`frigate-nvr`](.agents/skills/frigate-nvr/SKILL.md) | Production-grade Frigate NVR configuration, homelab deployment, and hardware-accelerated surveillance automation. Covers real-time RTSP/WebRTC camera streaming wi... |
| [`home-server-management`](.agents/skills/home-server-management/SKILL.md) | Manage homelab infrastructure and home servers. Use for Docker compose lifecycle orchestration, container health checks, automated disk space pruning, storage hea... |
| [`hostinger-ssh`](.agents/skills/hostinger-ssh/SKILL.md) | SSH into Hostinger shared hosting (u244089748 on 145.79.210.59:65002) via OpenSSH with key auth. Exec remote commands, upload/download via scp. Never stores passw... |
| [`ichome-ssh`](.agents/skills/ichome-ssh/SKILL.md) | Secure agent SSH bridge to the personal home server ICHOME (IC200@3.6). Provides auto-routing over LAN (192.168.1.4) or Tailscale WireGuard mesh (100.111.215.107)... |
| [`omarchy`](.agents/skills/omarchy/SKILL.md) | REQUIRED for end-user customization of Linux desktop, window manager, or system config. Use when editing ANY file in ~/.config/, ~/.config/hypr/, ~/.config/omarch... |
| [`omarchy-app`](.agents/skills/omarchy-app/SKILL.md) | Build a new desktop app for Omarchy the way Omarchy's own apps are built (Hype, Monologue, Omacut): C++ and Qt Quick, compiled with qmake6 and make into a single... |
