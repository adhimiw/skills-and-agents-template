---
name: git-workflow
description: Advanced Git workflows and version control practices based on iuliandita/skills/git. Covers atomic commits with interactive staging, rebase workflows with autosquash, merge conflict diagnosis and resolution with rerere and diff3, pull request hygiene with stacked branches, and self-hosted Forgejo integration.
---

# Advanced Git Workflow & Version Control

## Overview

`git-workflow` provides comprehensive workflows, recovery procedures, and standards for high-discipline software development. Based on `iuliandita/skills/git`, this skill enforces atomic commits, linear history rebasing, deterministic merge conflict resolution using `diff3` and `rerere`, structured pull request slicing, and integration with self-hosted Forgejo/Gitea instances.

---

## Triggers & When to Use

Activate this skill when:
- Staging and structuring code changes into atomic, reviewable commits.
- Performing interactive rebases (`git rebase -i`), squashing, or autosquashing fixup commits.
- Diagnosing and resolving complex 3-way merge conflicts.
- Slicing large pull requests into manageable stacked branches.
- Interacting with self-hosted Forgejo repositories, Forgejo Actions CI, or the `tea` CLI.
- Recovering lost commits, stashes, or unreferenced branches using `git reflog` and `git fsck`.

---

## 1. Atomic Commits & Interactive Staging

An atomic commit represents a single logical unit of change that builds, passes tests, and can be reverted cleanly without breaking unrelated code.

### 1.1 Conventional Commits Format
Follow the Conventional Commits specification:
```
<type>(<optional scope>): <imperative summary>

[optional detailed body explaining WHY, not just WHAT]

[optional issue reference: Fixes #123, Closes #456]
```

**Allowed Types:**
- `feat`: New feature or user-facing capability.
- `fix`: Bug fix.
- `refactor`: Code change that neither fixes a bug nor adds a feature.
- `perf`: Performance improvement.
- `test`: Adding or correcting tests.
- `docs`: Documentation changes only.
- `chore`: Build system, CI, dependencies, or tool updates.

### 1.2 Interactive Staging (Hunk Slicing)
When working on multiple files or distinct changes in a single file, never use blind `git add .`.

```bash
# Interactively stage hunks
git add -p path/to/file.ext
```

**Interactive Hunk Prompt Commands:**
- `y`: Stage this hunk.
- `n`: Do not stage this hunk.
- `q`: Quit; do not stage this hunk or any of the remaining ones.
- `s`: Split the current hunk into smaller hunks.
- `e`: Manually edit the current hunk.
- `d`: Do not stage this hunk or any of the later hunks in the file.

---

## 2. Rebasing Workflows & History Hygiene

Maintain a clean, understandable, and bisectable commit graph using rebase-driven workflows.

### 2.1 Trunk-Based Syncing with Upstream
Always pull upstream updates using rebase to prevent unnecessary merge bubbles:
```bash
# Fetch and rebase feature branch onto latest main
git fetch origin main
git rebase origin/main
```

### 2.2 Fixup & Autosquash Workflow
Create focused fixup commits during code review without disturbing commit messages:

```bash
# 1. Identify target commit hash to fix (e.g. abc1234)
git log --oneline -5

# 2. Stage fix changes and commit with --fixup flag
git add path/to/fixed_file.py
git commit --fixup abc1234

# 3. Automatically fold all fixup commits into their targets
git rebase -i --autosquash origin/main
```

### 2.3 Interactive Rebasing (`git rebase -i`)
Clean up local branch history before opening a pull request:
```bash
git rebase -i HEAD~5
```

```
pick a1b2c3d feat(auth): add JWT verification middleware
fixup e4f5g6h fix typo in token validation logic
reword h7i8j9k refactor(user): extract token parser to helper
squash l1m2n3o test(auth): add expired token test cases
```
- `pick`: Keep the commit.
- `reword`: Keep the commit, but edit the commit message.
- `edit`: Pause rebase to amend the commit contents.
- `squash`: Meld commit into previous commit; keep and combine log messages.
- `fixup`: Meld commit into previous commit; discard this commit's message.
- `drop`: Remove the commit entirely.

---

## 3. Merge Conflict Diagnosis & Resolution

### 3.1 Superior Conflict Visibility: `zdiff3`
Standard Git conflict markers only show "ours" and "theirs", leaving out the common ancestor. Configure `zdiff3` to display the base version:

```bash
# Enable zdiff3 conflict style globally
git config --global merge.conflictstyle zdiff3
```

Conflict markers will now display:
```
<<<<<<< HEAD (Current branch)
const timeout = 5000;
||||||| base (Common ancestor)
const timeout = 1000;
=======
const timeout = 3000;
>>>>>>> feature-branch (Incoming change)
```

### 3.2 Automated Conflict Resolution Reuse (`git rerere`)
`rerere` (Reuse Recorded Resolution) remembers how you resolved a hunk conflict and applies the exact same resolution automatically during future rebases:

```bash
# Enable rerere globally
git config --global rerere.enabled true
git config --global rerere.autoupdate true
```

### 3.3 Conflict Investigation Commands
When a merge or rebase stops on a conflict:
```bash
# View list of conflicted unmerged files
git status --short | grep "^UU"

# Find the common ancestor commit
git merge-base HEAD MERGE_HEAD

# View commit history that touched the conflicted file on both branches
git log --merge -p path/to/conflicted_file.py

# Abort cleanly if the conflict is unmanageable or branch strategy was wrong
git merge --abort
# Or during rebase:
git rebase --abort
```

---

## 4. Pull Request Hygiene & Slicing

Keep pull requests small, focused, and reviewable (<400 lines of changed code).

### 4.1 Slicing Stacked Branches
When building a large feature, split it into dependent slices:
```
main ──●──●──● (base)
        ╲
         ●──● feat/data-models (PR #1)
              ╲
               ●──● feat/api-routes (PR #2 -> targets PR #1)
                    ╲
                     ●──● feat/frontend-ui (PR #3 -> targets PR #2)
```

Updating stacked branches after upstream changes:
```bash
# When PR #1 is merged into main, rebase PR #2 onto main:
git rebase --onto origin/main feat/data-models feat/api-routes
```

### 4.2 PR Template Standard
```markdown
## Summary
Brief explanation of what this PR accomplishes.

## Motivation & Context
Why is this change required? What problem does it solve?
Fixes #<ISSUE_NUMBER>

## Changes Proposed
- Bullet points detailing key modifications.
- Breaking changes highlighted.

## Testing & Verification
- Unit test suite: `npm test` / `pytest`
- Manual verification steps performed:
  1. Action taken
  2. Observed outcome
```

---

## 5. Self-Hosted Forgejo (and Gitea) Integration

Forgejo is the community-driven, self-hosted Git platform. Interact with Forgejo directly using Git protocols, webhooks, and the `tea` CLI.

### 5.1 Authenticating `tea` CLI with Forgejo
```bash
# Add a Forgejo instance login
tea login add \
  --name homelab-forgejo \
  --url https://git.lab.internal \
  --token <YOUR_PERSONAL_ACCESS_TOKEN>

# Verify connection
tea whoami
```

### 5.2 Operating Repositories and PRs via Forgejo CLI
```bash
# List open issues on current repository
tea issues

# Create a pull request targeting main branch
tea pr create \
  --title "feat(backup): add restic snapshot automation" \
  --description "Implements automated daily encrypted backups for Docker volumes." \
  --target main

# Review and merge a pull request
tea pr list
tea pr merge 42 --squash
```

### 5.3 Forgejo Actions CI Workflow Template
Forgejo Actions executes container-based CI workflows compatible with GitHub Actions syntax:

```yaml
# .forgejo/workflows/ci.yaml
name: Continuous Integration

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: native
    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run Linters & Security Audit
        run: |
          ruff check .
          bandit -r . -ll

      - name: Run Test Suite
        run: |
          pytest --cov=. --cov-report=term-missing
```

---

## 6. Disaster Recovery & Safety Net Reference

### 6.1 Recovering from Mistaken Hard Reset or Rebase (`git reflog`)
Git almost never deletes committed data immediately. Use the reference log to recover any lost state:

```bash
# 1. View reflog of all recent HEAD movements
git reflog --date=relative -20

# 2. Locate the commit before the bad operation (e.g., HEAD@{2})
# 3. Restore to a new recovery branch
git checkout -b recovery-branch HEAD@{2}
```

### 6.2 Recovering Accidentally Dropped Stashes
```bash
# Find all unreachable dangling commit objects
git fsck --lost-found | grep commit

# Inspect dangling commit to find the lost stash
git log -1 --stat <DANGLING_COMMIT_HASH>

# Apply the recovered commit
git cherry-pick <DANGLING_COMMIT_HASH>
```

### 6.3 Essential Git Configuration Aliases
Add these aliases to `~/.gitconfig` for maximum efficiency:

```ini
[alias]
    st = status -sb
    co = checkout
    br = branch
    ci = commit
    # Graph view showing branch topology and commit hashes
    lg = log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
    # Quick fixup commit without editor prompt
    fix = commit --fixup
    # Push current branch safely with lease
    praise = push --force-with-lease
    # Show what changed in the last commit
    last = log -1 HEAD --stat
    # View conflicted files
    conflicts = diff --name-only --diff-filter=U
```
