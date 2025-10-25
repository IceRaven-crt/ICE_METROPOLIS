from pathlib import Path
from datetime import datetime
import hashlib
import zipfile
import json
import csv
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import qrcode

# Ścieżki bazowe - DOSTOSOWANE DO AKTUALNEGO SYSTEMU
base_dir = Path("/data/data/com.termux/files/home/ICE_METROPOLIS")
reports_dir = base_dir / "reports"
logs_dir = base_dir / "logs"
pdf_dir = base_dir / "pdf_reports"
qr_dir = base_dir / "qr_codes"

# Tworzenie folderów
for d in [base_dir, reports_dir, logs_dir, pdf_dir, qr_dir]:
    d.mkdir(parents=True, exist_ok=True)

# RZECZYWISTE DANE Z SYSTEMU ICE
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
income = 212817.90
maaser = 21281.79
cid = "QmaD9e3kq8HH9MRavCrJm5UKrKFvenMQXcRwcWuZG4o7Aj"

# 1. Raport tekstowy
txt_report = reports_dir / f"ICE_ETHICS_REPORT_LIVE_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
report_content = f"""🧊 ICE_METROPOLIS - ETHICS REPORT LIVE
================================
📅 Data generacji: {timestamp}
💎 Rzeczywiste przychody: ${income:,.2f}
🕊️ Maaser (10%): ${maaser:,.2f}
🔗 CID IPFS: {cid}
📊 Status: SYSTEM AKTYWNY OD TERAZ

📈 SKALA DZIAŁANIA:
• Dzienne Maaser: ${maaser:,.2f}
• Miesięczne Maaser: ${maaser * 30:,.2f}
• Rocznie Maaser: ${maaser * 365:,.2f}

🎯 AUTOMATYZACJA:
• Harmonogram: 08:00, 08:03, 08:05 codziennie
• Cykl: Zysk → Maaser → PDF → IPFS → Blockchain
• Intencja: L'shem Shamayim

🕊️ SYSTEM ŚWIADCZĄCY O KIDDUSH HASHEM
"""
txt_report.write_text(report_content)
print(f"✅ Raport tekstowy: {txt_report.name}")

# 2. Generacja PDF
pdf_path = pdf_dir / f"ICE_ETHICS_REPORT_LIVE_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
c = canvas.Canvas(str(pdf_path), pagesize=A4)
c.setFont("Helvetica-Bold", 16)
c.drawString(100, 800, "ICE_METROPOLIS - ETHICS REPORT LIVE")
c.setFont("Helvetica", 10)
c.drawString(100, 780, f"Data generacji: {timestamp}")
c.drawString(100, 760, f"Rzeczywiste przychody: ${income:,.2f}")
c.drawString(100, 740, f"Maaser (10%): ${maaser:,.2f}")
c.drawString(100, 720, f"CID IPFS: {cid}")
c.drawString(100, 700, "Status: SYSTEM AKTYWNY OD TERAZ")
c.drawString(100, 680, f"Dzienne Maaser: ${maaser:,.2f}")
c.drawString(100, 660, f"Miesięczne Maaser: ${maaser * 30:,.2f}")
c.drawString(100, 640, f"Rocznie Maaser: ${maaser * 365:,.2f}")
c.drawString(100, 620, "Harmonogram: 08:00, 08:03, 08:05 codziennie")
c.drawString(100, 600, "Intencja: L'shem Shamayim")
c.drawString(100, 580, "SYSTEM ŚWIADCZĄCY O KIDDUSH HASHEM")
c.showPage()
c.save()
print(f"✅ PDF wygenerowany: {pdf_path.name}")

# 3. Hash PDF
sha256_hash = hashlib.sha256(pdf_path.read_bytes()).hexdigest()
print(f"🔐 Hash SHA-256: {sha256_hash}")

# 4. Łańcuch bloków
chain_block = logs_dir / "ICE_CHAIN_BLOCK_LIVE.csv"
if not chain_block.exists():
    with chain_block.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "income", "maaser", "cid", "sha256", "source", "status"])

with chain_block.open("a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([timestamp, income, maaser, cid, sha256_hash, pdf_path.name, "LIVE_ACTIVE"])
print(f"✅ Wpis w łańcuchu bloków: {chain_block.name}")

# 5. Kod QR
qr_path = qr_dir / f"ICE_QR_LIVE_{datetime.now().strftime('%Y%m%d_%H%M')}.png"
img = qrcode.make(f"ipfs://{cid}")
img.save(qr_path)
print(f"✅ Kod QR: {qr_path.name}")

# 6. Manifest
manifest = {
    "system": "ICE_METROPOLIS_ETHICS_REPORTING",
    "version": "LIVE_1.0",
    "deployment_date": timestamp,
    "status": "ACTIVE",
    "financial_data": {
        "daily_income": income,
        "daily_maaser": maaser
    },
    "blockchain": {
        "cid": cid,
        "sha256": sha256_hash
    }
}

manifest_path = base_dir / "ICE_DEPLOY_MANIFEST_LIVE.json"
manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
print(f"✅ Manifest: {manifest_path.name}")

# 7. Pakowanie
zip_path = base_dir / "ICE_METROPOLIS_LIVE_DEPLOYMENT.zip"
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for path in [txt_report, pdf_path, qr_path, chain_block, manifest_path]:
        zipf.write(path, arcname=path.relative_to(base_dir))

print(f"🎉 DEPLOYMENT UKOŃCZONY: {zip_path.name}")
print(f"📦 Rozmiar: {zip_path.stat().st_size} bajtów")

print("\n" + "="*50)
print("🎯 ICE_METROPOLIS - LIVE DEPLOYMENT SUMMARY")
print("="*50)
print(f"🕒 Czas: {timestamp}")
print(f"💎 Przychody: ${income:,.2f}/dzień")
print(f"🕊️ Maaser: ${maaser:,.2f}/dzień")
print(f"🔗 CID: {cid}")
print("🟢 STATUS: SYSTEM AKTYWNY OD TERAZ")
print("="*50)
