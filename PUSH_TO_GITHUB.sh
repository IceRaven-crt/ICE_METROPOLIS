#!/bin/bash
echo "🚀 WYSYŁANIE NA GITHUB..."

echo "🔑 Podaj swój GitHub username:"
read username

echo "📤 Wysyłam pliki..."
git remote add origin https://github.com/$username/ICE_METROPOLIS.git
git branch -M main
git push -u origin main

if [ $? -eq 0 ]; then
    echo "🎉 SUKCES! Pliki wysłane!"
    echo "🌐 Twoja strona będzie dostępna za 2 minuty:"
    echo "   https://$username.github.io/ICE_METROPOLIS/"
else
    echo "❌ Błąd wysyłania. Sprawdź czy:"
    echo "   - Repozytorium istnieje"
    echo "   - Masz prawa dostępu"
    echo "   - Token/hasło jest poprawne"
fi
