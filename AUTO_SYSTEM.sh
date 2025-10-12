#!/usr/bin/env bash
echo "🔁 AUTO SYSTEM RUNNING..."
zip -r "ICE_BACKUP_$(date +%Y%m%d_%H%M).zip" .
sha256sum ICE_BACKUP_*.zip > HASH_SHA256.txt
echo "✅ Auto-backup complete. Hash updated."
