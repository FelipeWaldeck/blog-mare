#!/bin/bash
# Hugo Blog Deploy Script - Push to trigger Cloudflare Pages auto-deploy

set -e

cd "$(dirname "$0")"

echo "Building Hugo site..."
hugo

echo "Committing build..."
git add -A
git commit -m "Auto-deploy $(date '+%Y-%m-%d %H:%M')" || echo "No changes to commit"

echo "Pushing to trigger Cloudflare Pages..."
git push origin master

echo "✅ Deployed! Check https://dash.cloudflare.com for build status."