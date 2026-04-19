#!/bin/bash

# Deploy script for Pixie's Pantry storefront
# Automates the generation and deployment of the storefront to GitHub Pages

# Exit on error
set -e

# Navigate to the project directory
cd /Users/dusty/Desktop/Pixies_Vape_Shop

# Generate the storefront
echo "Generating storefront..."
python3 generate_storefront.py

# Check if the index.html was generated
if [ ! -f "index.html" ]; then
    echo "Error: index.html was not generated."
    exit 1
fi

# Stash any changes that aren't index.html to avoid committing them
echo "Stashing non-index.html changes..."
git stash push --keep-index --include-untracked -- "*:!index.html" || true

# Commit and push only index.html
echo "Committing and pushing index.html..."
git add index.html

# Use a timestamp for the commit message
COMMIT_MESSAGE="Update storefront - $(date +"%Y-%m-%d %H:%M:%S")"
git commit -m "$COMMIT_MESSAGE" || {
    echo "No changes to commit."
    git stash pop || true
    exit 0
}

# Push to GitHub
git push origin main

# Force a redeploy by pushing an empty commit
echo "Forcing GitHub Pages redeploy..."
git commit --allow-empty -m "Trigger GitHub Pages redeploy"
git push origin main

# Restore stashed changes (if any)
echo "Restoring stashed changes..."
git stash pop || true

echo "Deployment complete! Check shop.pixiespantryshop.com in a few minutes."