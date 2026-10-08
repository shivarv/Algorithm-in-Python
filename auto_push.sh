#!/bin/bash
REPO="/Users/shiva/Desktop/git hub/Algorithm-in-Python"
cd "$REPO" || exit 1

git add .

# Skip commit if nothing changed (otherwise git commit errors out)
if git diff --cached --quiet; then
  echo "$(date): nothing to commit"
  exit 0
fi

git commit -m "$(date +%Y-%m-%d)"
git push -u origin main
echo "$(date): pushed"
