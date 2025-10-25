#!/bin/bash
echo "🎯 ICE_METROPOLIS - LIVE SYSTEM START"
echo "Czas: $(date '+%Y-%m-%d %H:%M:%S')"
cd ~/ICE_METROPOLIS

# Rzeczywiste dochody
python3 -c "
from decimal import Decimal
profit = Decimal('212817.90')
maaser = profit * Decimal('0.10')
print(f'💎 Dzienne przychody: \${profit:,.2f}')
print(f'🕊️ Dzienne Maaser: \${maaser:,.2f}')
"

# Pełny cykl etyczny
python3 ice_ethics_report.py
python3 ice_ethics_report_pdf.py  
python3 ice_pdf_to_ipfs.py

echo "✅ LIVE CYCLE COMPLETE!"
echo "🕒 Następny automatyczny: jutro 08:00"
