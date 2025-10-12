from pathlib import Path
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import hashlib
import json
import zipfile
import qrcode

# Konfiguracja ścieżek - poprawiam dla Termux
base_path = Path("/data/data/com.termux/files/home/ICE_METROPOLIS/ICE_METROPOLIS_NFT")
web_html = base_path / "ICE_METROPOLIS_FINAL.html"
pdf_path = base_path / "ICE_METROPOLIS_MANIFEST.pdf"
qr_path = base_path / "ICE_METROPOLIS_QR.png"
zip_path = base_path / "ICE_METROPOLIS_FINAL.zip"
metadata_path = base_path / "NFT_METADATA.json"

# Utwórz katalog
base_path.mkdir(parents=True, exist_ok=True)

# Używamy prawdziwego index.html
html_content = Path("index.html").read_text(encoding="utf-8")
web_html.write_text(html_content, encoding="utf-8")

# Oblicz SHA-256
sha256_hash = hashlib.sha256(web_html.read_bytes()).hexdigest()

# Generowanie QR z prawdziwym URL
qr = qrcode.make("https://ice-metropolis-xyz123.netlify.app")
qr.save(qr_path)

# Tworzenie PDF manifestu (uproszczone bez Image)
doc = SimpleDocTemplate(str(pdf_path), pagesize=A4)
styles = getSampleStyleSheet()
elements = [
    Paragraph("🧊 ICE_METROPOLIS_MANIFEST", styles["Heading1"]),
    Spacer(1, 12),
    Paragraph("System: ICE_METROPOLIS", styles["Normal"]),
    Paragraph("Status: ONLINE | BITCOMAT ACTIVE", styles["Normal"]),
    Paragraph("System ID: C0C95A53", styles["Normal"]),
    Paragraph(f"SHA-256: {sha256_hash}", styles["Normal"]),
    Spacer(1, 12),
    Paragraph("Autoryzacja: Paweł Szczurowski / ICE_RAVEN", styles["Normal"]),
    Paragraph("Dziedzic: Nikoś", styles["Normal"]),
    Spacer(1, 12),
    Paragraph("QR Code: ICE_METROPOLIS_QR.png", styles["Normal"]),
    Spacer(1, 12),
    Paragraph("Data wygenerowania: " + datetime.now().isoformat(), styles["Italic"]),
]
doc.build(elements)

# Metadata NFT
metadata = {
    "name": "ICE_METROPOLIS NFT",
    "description": "Dashboard statusowy systemu ICE — LIVE status + Bitcomat",
    "author": "Paweł Szczurowski / ICE_RAVEN",
    "sha256": sha256_hash,
    "url": "https://ice-metropolis-xyz123.netlify.app",
    "edition": "1/1",
    "tags": ["ICE", "Metropolis", "Dashboard", "NFT", "Bitcomat", "2137"],
    "heir": "Nikoś",
    "preservation": "Eternal"
}
metadata_path.write_text(json.dumps(metadata, indent=4), encoding="utf-8")

# ZIP finalny
with zipfile.ZipFile(zip_path, "w") as zipf:
    zipf.write(web_html, arcname=web_html.name)
    zipf.write(pdf_path, arcname=pdf_path.name)
    zipf.write(qr_path, arcname=qr_path.name)
    zipf.write(metadata_path, arcname=metadata_path.name)

print("✅ NFT PACKAGE GENERATED!")
print(f"📦 ZIP: {zip_path}")
print(f"🔗 URL: https://ice-metropolis-xyz123.netlify.app")
print(f"🔐 SHA256: {sha256_hash}")
