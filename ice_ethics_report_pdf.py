#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ICE_METROPOLIS · Ethics Report PDF Generator
Konwersja raportu tekstowego do PDF z QR i hash SHA-256.
"""

from pathlib import Path
from datetime import datetime
import hashlib
import qrcode
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
import subprocess
import sys

# Sprawdzamy czy reportlab jest zainstalowany
try:
    from reportlab.lib.pagesizes import A4
except ImportError:
    print("❌ Brak biblioteki reportlab. Instalujemy...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])
    from reportlab.lib.pagesizes import A4

# Sprawdzamy czy qrcode jest zainstalowany
try:
    import qrcode
except ImportError:
    print("❌ Brak biblioteki qrcode. Instalujemy...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "qrcode[pil]"])
    import qrcode

# Konfiguracja
BASE_DIR = Path.home() / "ICE_METROPOLIS"
REPORT_DIR = BASE_DIR / "reports"
PDF_DIR = BASE_DIR / "pdf_reports"
QR_DIR = BASE_DIR / "qr"

for d in (PDF_DIR, QR_DIR):
    d.mkdir(parents=True, exist_ok=True)

styles = getSampleStyleSheet()
style_title = styles["Heading1"]
style_sub = styles["Heading2"]
style_text = styles["Normal"]

def sha256sum(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def generate_ethics_pdf(txt_report: Path):
    if not txt_report.exists():
        print(f"❌ Brak pliku raportu: {txt_report}")
        return None

    report_hash = sha256sum(txt_report)
    qr_path = QR_DIR / f"{txt_report.stem}.png"
    qrcode.make(report_hash).save(qr_path)

    pdf_path = PDF_DIR / f"{txt_report.stem}.pdf"
    doc = SimpleDocTemplate(str(pdf_path), pagesize=A4, 
                          rightMargin=36, leftMargin=36, 
                          topMargin=48, bottomMargin=36)
    story = []

    story.append(Paragraph("🧊 ICE_METROPOLIS – ETHICAL IMPACT REPORT", style_title))
    story.append(Paragraph(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), style_text))
    story.append(Spacer(1, 12))

    text = txt_report.read_text(encoding="utf-8")
    for line in text.splitlines():
        if line.strip():
            story.append(Paragraph(line, style_text))

    story.append(Spacer(1, 12))
    story.append(Paragraph("───────────────────────────────", style_text))
    story.append(Paragraph("🔐 HASH INTEGRITY", style_sub))
    story.append(Paragraph(f"SHA-256: {report_hash}", style_text))
    story.append(Spacer(1, 12))

    story.append(Paragraph("📱 QR Verification:", style_sub))
    story.append(Image(str(qr_path), width=120, height=120))
    story.append(Spacer(1, 24))

    story.append(Paragraph("📜 Signed: ICE_RAVEN_2137", style_text))
    story.append(Paragraph("This report is a verified record within ICE_METROPOLIS.", style_text))

    doc.build(story)
    print(f"✅ PDF utworzony: {pdf_path}")
    return pdf_path, report_hash

if __name__ == "__main__":
    latest = sorted(REPORT_DIR.glob("ICE_ETHICS_REPORT_*.txt"))
    if latest:
        generate_ethics_pdf(latest[-1])
    else:
        print("❌ Nie znaleziono plików raportów")
