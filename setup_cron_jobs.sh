#!/bin/bash
# Konfiguracja automatycznych cron jobs dla ICE

echo "⏰ KONFIGURUJĘ AUTOMATYCZNE RAPORTOWANIE ICE..."

# Sprawdź czy cron już skonfigurowany
if crontab -l 2>/dev/null | grep -q "ice_daily_report"; then
    echo "✅ Cron jobs już skonfigurowane"
else
    # Dodaj cron jobs
    (crontab -l 2>/dev/null; echo "0 8 * * * cd /data/data/com.termux/files/home/ICE_METROPOLIS && ./ice_daily_report.sh") | crontab -
    (crontab -l 2>/dev/null; echo "0 20 * * * cd /data/data/com.termux/files/home/ICE_METROPOLIS && ./ice_daily_report.sh now") | crontab -
    (crontab -l 2>/dev/null; echo "0 * * * * cd /data/data/com.termux/files/home/ICE_METROPOLIS && python3 ice_health_check.py") | crontab -
    
    echo "✅ Dodano cron jobs:"
    echo "   🕗 08:00 - Daily Morning Report"
    echo "   🕗 20:00 - Daily Evening Report" 
    echo "   🕐 Co godzinę - Health Check"
fi

# Pokaz aktualne cron jobs
echo ""
echo "📅 AKTUALNE CRON JOBS:"
crontab -l 2>/dev/null | grep -E "(ice|ICE)" || echo "Brak ice cron jobs"
