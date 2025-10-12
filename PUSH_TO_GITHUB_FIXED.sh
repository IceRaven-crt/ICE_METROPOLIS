#!/bin/bash
echo "🚀 POPRAWNE WYSYŁANIE NA GITHUB"

# Usuń stary remote jeśli istnieje
git remote remove origin 2>/dev/null

echo "🔑 Podaj swój GitHub username:"
read username

echo "📝 Tworzę nowe repozytorium przez GitHub API..."
echo "ℹ️  Jeśli repo już istnieje, pomiń ten krok"

# Sprawdź czy repozytorium istnieje
response=$(curl -s -o /dev/null -w "%{http_code}" "https://github.com/$username/ICE_METROPOLIS")

if [ "$response" != "200" ]; then
    echo "❌ Repozytorium ICE_METROPOLIS nie istnieje użytkownika $username"
    echo "🌐 Wejdź na: https://github.com/new"
    echo "🏷️ Stwórz repozytorium: ICE_METROPOLIS"
    echo "📝 Public, z README"
    echo ""
    echo "⏳ Czy utworzyłeś repozytorium? (tak/nie)"
    read created
    if [ "$created" != "tak" ]; then
        echo "❌ Najpierw utwórz repozytorium na GitHub!"
        exit 1
    fi
fi

echo "📤 Wysyłam pliki..."
git remote add origin "https://github.com/$username/ICE_METROPOLIS.git"
git branch -M main

echo "🔐 Uwierzytelnianie..."
echo "💡 Użyj Personal Access Token jeśli masz 2FA włączone"
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 SUKCES! Pliki wysłane!"
    echo "🌐 Twoja strona będzie dostępna za 2 minuty:"
    echo "   https://$username.github.io/ICE_METROPOLIS/"
    echo ""
    echo "📋 OSTATECZNY KROK:"
    echo "1. Wejdź na: https://github.com/$username/ICE_METROPOLIS/settings/pages"
    echo "2. Włącz GitHub Pages: Branch: main, Folder: / (root)"
    echo "3. Poczekaj 2 minuty"
else
    echo "❌ Błąd wysyłania."
    echo "💡 Wskazówki:"
    echo "   - Utwórz repozytorium na GitHub"
    echo "   - Użyj Personal Access Token zamiast hasła"
    echo "   - Sprawdź czy repo jest publiczne"
fi
