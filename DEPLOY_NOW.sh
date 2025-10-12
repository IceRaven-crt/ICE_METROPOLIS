#!/bin/bash
echo "🧊 FINALNY DEPLOYMENT ICE_METROPOLIS"
echo "==================================="

# Usuń stary remote
git remote remove origin 2>/dev/null

# Ustaw poprawny remote
git remote add origin https://github.com/IceRaven-crt/ICE_METROPOLIS.git
git branch -M main

echo "📤 Wysyłam pliki na GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 SUKCES! DEPLOYMENT UDANY!"
    echo "🌐 TWOJA STRONA:"
    echo "   https://iceraven-crt.github.io/ICE_METROPOLIS/"
    echo ""
    echo "📋 OSTATECZNY KROK:"
    echo "1. Wejdź na: https://github.com/IceRaven-crt/ICE_METROPOLIS/settings/pages"
    echo "2. Włącz GitHub Pages:"
    echo "   - Source: Deploy from branch"
    echo "   - Branch: main"
    echo "   - Folder: / (root)"
    echo "3. Zapisz i poczekaj 2 minuty"
    echo ""
    echo "🧊 SYSTEM ICE BĘDZIE LIVE!"
else
    echo "❌ Błąd! Sprawdź czy:"
    echo "   - Repozytorium ICE_METROPOLIS istnieje"
    echo "   - Masz prawa dostępu"
    echo "   - Używasz Personal Access Token jeśli masz 2FA"
fi
