#!/usr/bin/env bash
echo "🌐 DEPLOYING ICE_METROPOLIS..."
npm install -g netlify-cli >/dev/null 2>&1
netlify deploy --prod --dir="$(pwd)" --message "ICE_METROPOLIS_DEPLOY_$(date +%Y%m%d)"
echo "✅ Deployment complete."
