#!/bin/bash
echo "🔄 Uruchamianie cyklu ICE_METROPOLIS Ethics..."
cd ~/ICE_METROPOLIS
python3 ice_ethics_report.py
python3 ice_ethics_report_pdf.py  
python3 ice_pdf_to_ipfs.py
echo "✅ Cykl etyczny zakończony!"
echo "💎 Dzienne przychody: \$212,817.90"
echo "🕊️ Dzienne Maaser: \$21,281.79"
