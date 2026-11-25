#!/usr/bin/env bash
set -euo pipefail

# Self-updating skill & private GitHub sync script
PORTFOLIO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
TEMPLATE_ROOT="/home/adhithan/Projects/skills-and-agents-template"
SKILL_REL=".agents/skills/portfolio-master"
STATE_FILE="$PORTFOLIO_ROOT/$SKILL_REL/references/project-state.md"

cd "$PORTFOLIO_ROOT"

VERSION="$(node -p "require('./package.json').version" 2>/dev/null || echo '1.0.0')"
TAG="$(git describe --tags --always 2>/dev/null || echo "v$VERSION")"
MODELS="$(ls server/models/*.js 2>/dev/null | xargs -n1 basename | sed 's/\.js$//' | tr '\n' ',' | sed 's/,$//; s/,/, /g')"
ROUTES="$(ls server/routes/*.js 2>/dev/null | xargs -n1 basename | sed 's/\.js$//' | tr '\n' ',' | sed 's/,$//; s/,/, /g')"
TEST_COUNT="$(grep -chE '^[[:space:]]*test\(' server/test/*.js 2>/dev/null | awk '{s+=$1} END{print s+0}')"
UPDATED_AT="$(date -Iseconds)"

cat > "$STATE_FILE" <<EOF
# Live Project State (Auto-Updated)

- **Synced At**: \`$UPDATED_AT\`
- **Package Version**: \`v$VERSION\`
- **Git Ref**: \`$TAG\`
- **Frontend**: React 19 + React Router + PWA + Capacitor 8 Android App (\`/\`, \`/resume\`, \`/admin\`)
- **Backend Models**: $MODELS
- **Backend Route Modules**: $ROUTES
- **Integration Test Cases**: $TEST_COUNT
EOF

echo "Updated $STATE_FILE"

# Mirror portfolio-master and updated portfolio skills cleanly into skills-and-agents-template (preserving other work-sorted skills)
if [ -d "$TEMPLATE_ROOT/.agents/skills" ]; then
  rsync -a --exclude '__pycache__' --exclude 'node_modules' --exclude '.git' --exclude '.venv' "$PORTFOLIO_ROOT/.agents/skills/" "$TEMPLATE_ROOT/.agents/skills/"
  echo "Synced skills to $TEMPLATE_ROOT/.agents/skills/"
fi

# Commit and push if git remotes exist (keeps private GitHub repos continuously backed up)
if git remote get-url origin >/dev/null 2>&1; then
  git add "$SKILL_REL"
  if ! git diff --cached --quiet; then
    git commit -m "chore(skill): auto-update portfolio-master state ($TAG)"
  fi
  git push origin HEAD --tags || echo "Warning: push failed for lab-portfolio"
fi

if [ -d "$TEMPLATE_ROOT/.git" ]; then
  (
    cd "$TEMPLATE_ROOT"
    if git remote get-url origin >/dev/null 2>&1; then
      git add .agents/skills
      if ! git diff --cached --quiet; then
        git commit -m "chore(skills): sync self-updating portfolio-master skill ($TAG)"
      fi
      git push origin HEAD || echo "Warning: push failed for skills-and-agents-template"
    fi
  )
fi
