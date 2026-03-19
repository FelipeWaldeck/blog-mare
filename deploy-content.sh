#!/bin/bash
# Mare Blog Auto-Deploy Script
# Runs weekly to deploy new content to blog.mare.run

set -e

BLOG_DIR="$HOME/.openclaw/workspace/blog-mare"

echo "=== Mare Blog Deploy ==="
echo "Date: $(date)"

cd "$BLOG_DIR"

# Build Hugo
echo "Building Hugo site..."
hugo --gc --minify

# Check if there are new posts
POST_COUNT=$(ls -1 content/posts/*.md 2>/dev/null | wc -l)
echo "Posts found: $POST_COUNT"

# Commit changes if any
if [[ $(git status --porcelain) ]]; then
    echo "Committing changes..."
    git add -A
    git commit -m "Auto-deploy $(date '+%Y-%m-%d %H:%M')" || echo "No changes to commit"
    
    echo "Deploying to Cloudflare Pages..."
    cd public
    
    # Deploy via wrangler - use token from environment or .dev.vars
    # Try to load from .dev.vars if not in environment
    if [ -z "$CLOUDFLARE_API_TOKEN" ] && [ -f "$HOME/.openclaw/workspace/cloudflare-mare/browser-renderer/.dev.vars" ]; then
        export CLOUDFLARE_API_TOKEN=$(grep "CF_API_TOKEN" "$HOME/.openclaw/workspace/cloudflare-mare/browser-renderer/.dev.vars" | cut -d'=' -f2)
    fi
    
    export CLOUDFLARE_ACCOUNT_ID="019659a790e2050c808616a4fb1ef4ca"
    
    # Clear deprecated CF_API_TOKEN if set
    unset CF_API_TOKEN
    
    wrangler pages deploy . --project-name=blog-mare --commit-dirty=true
    
    echo "✅ Deployed successfully!"
else
    echo "No changes to deploy"
fi

echo "=== Done ==="
