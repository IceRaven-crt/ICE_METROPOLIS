#!/bin/bash
echo "🧊 ICE METROPOLIS - AUTO GITHUB DEPLOY"

# Sprawdź czy git jest skonfigurowany
if ! git config --get user.name; then
    git config --global user.name "Paweł Szczurowski"
    git config --global user.email "ice@metropolis.com"
fi

# Push do repo
echo "🚀 Wysyłam kod na GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo "✅ KOD WYSŁANY NA GITHUB!"
    echo "🔗 Teraz aktywuj GitHub Pages:"
    echo "1. Wejdź w repo na GitHub.com"
    echo "2. Settings → Pages → Branch: main → Save"
    echo "3. Poczekaj 2 minuty"
    echo "4. Odbierz URL i wklej tutaj"
else
    echo "❌ Najpierw musisz dodać remote repo!"
    echo "🎯 Wykonaj: git remote add origin TWOJE_REPO_URL"
fi
