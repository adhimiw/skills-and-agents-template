# Full Skills & Agent Starter Template

A complete, production-grade template containing **70+ specialized agent skills**, deterministic engineering rules, anti-slop filters, art direction engines, design intelligence, and verification scripts for autonomous coding agents (**Claude Code, Google Antigravity, Cursor, Windsurf, OpenCode**).

---

## 📦 What's Included

```text
skills-and-agents-template/
├── .agents/
│   ├── rules/
│   │   ├── antislop.md                 # Core anti-slop rules (anti-generic AI aesthetics)
│   │   ├── engineering-workflow.md     # Gentle-AI work-unit commits & scope recon
│   │   ├── design-taste-quality.md     # Taste-Skill craft laws & typography guidelines
│   │   └── ui-ux-standards.md          # WCAG 2.2 AA & interaction standards
│   └── skills/                         # Canonical library of 70 fully dereferenced skills
├── .claude/
│   └── skills -> ../.agents/skills     # Direct symlink for Claude Code
├── skills -> .agents/skills            # Universal convenience symlink
├── AGENTS.md                           # Universal master instructions for coding agents
├── GEMINI.md                           # Master instructions for Google Antigravity / Gemini
├── DESIGN.md                           # Starter design system & brand contract
├── package.json                        # Development scripts, linters & skill test runners
├── vite.config.js                      # Pre-configured Vite configuration
└── .gitignore                          # Clean standard ignore rules
```

---

## 🌟 The 9 Core Pillars

1. **Anti-Slop** (`miqdadbadjuber/anti-slop`): Eliminates generic AI tropes, repetitive SaaS cards, fake metrics, unstyled contrast issues, and hallucinated marketing fluff.
2. **Taste-Skill** (`leonxlnx/taste-skill`): Art direction engine distilled from 247 award-winning websites with automated headless browser inspection (`inspect.mjs`), rule linter (`lint.mjs`), and direction dealing (`draw.mjs`).
3. **UI/UX Pro Max** (`nextlevelbuilder/ui-ux-pro-max-skill`): Zero-network local design database covering 79 styles, 192 color palettes, 74 font pairings, and 119 UX guidelines (`search.py`).
4. **Gentle-AI** (`Gentleman-Programming/gentle-ai`): Deterministic engineering environment with work-unit commits (< 400 lines), cognitive load reduction, and PR staging.
5. **Top UI/UX Engineering Skills** (`snyk.io/articles/top-claude-skills-ui-ux-engineers/`):
   - **Anthropic Frontend Design**: Creative lead guidance for distinctive, authentic aesthetics.
   - **Vercel Guidelines & React Best Practices**: 70 rules for optimal React/Next.js performance and composition patterns.
   - **AccessLint Accessibility Suite**: Automated and manual WCAG 2.2 AA/AAA accessibility audits.
   - **Bencium UX Designer**: Typography-led, human-centered innovative UX design.
6. **Editorial Visuals & 3D Immersion**:
   - **Diagram Design** (`cathrynlavery/diagram-design`): 45 visual diagram and schematic formats rendered as self-contained SVG/HTML.
   - **Dioramas** (`blendi-remade/dioramas`): Cinematic 3D landing page framework (Three.js r186, N8AO, GSAP, Lenis, AgX tone mapping).
7. **Engineering Reliability Runtime** (`udaysharmadev/Gravitas`): Model-agnostic reliability runtime with 6 invariants, scope recon, and post-mutation verification.
8. **App Cloning & Reverse-Engineering** (`Jakeschincariol/replica-skill`): 11 clean-room skills to reverse-engineer, design, test, brand, launch, and monetize web apps without touching proprietary code or assets.
9. **Visual & Audio Verification Engine** (`oxbshw/watch-skill`): Video/audio ingestion, scene-aware frame OCR, persistent index, verification contracts, and THE LOOP (capture -> critique -> fix -> verify).

---

## 🚀 How to Use in Any New Project

### 1. Extract into Your Project Root
Copy the contents of this template into your new project directory:
```bash
unzip skills-and-agents-template.zip -d my-new-project/
cd my-new-project
```

### 2. Install Development Dependencies
```bash
npm install
```

### 3. Initialize Git & Start Building
```bash
git init
git add .
git commit -m "chore: setup agent skills and project configuration"
```

### 4. Tell Your Agent to Activate the Skills
Whenever you prompt your coding agent (Claude Code, Antigravity, Cursor, etc.), simply say:
> *"Read AGENTS.md, follow the anti-slop rules and skills, and help me build [your project feature]..."*

The agent will automatically read `AGENTS.md`, adhere to the rules in `.agents/rules/`, and invoke the relevant skills from `.agents/skills/`.

---

## 🛠️ Handy CLI Commands Included

- **Art Direction Dealer**:
  ```bash
  npm run taste:draw -- --sector saas --brief "Your website brief" --options 3
  ```
- **Run Headless Browser Quality Gate**:
  ```bash
  npm run taste:inspect index.html
  ```
- **Lint Code Against Banned AI Tells & Anti-Slop Violations**:
  ```bash
  npm run taste:lint
  ```
- **Query UI/UX Intelligence**:
  ```bash
  npm run uiux:search "dark luxury fashion" -- --domain style
  npm run uiux:search "checkout form best practices" -- --domain ux
  ```
- **Check Color Contrast (WCAG 2.2 AA/AAA)**:
  ```bash
  npm run a11y:contrast "#FFFFFF" "#0D1117"
  ```
