#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ICE_METROPOLIS · PDF → IPFS Uploader
Automatyczny upload najnowszego raportu PDF do lokalnego IPFS i zapis CID w rejestrze ICE_CHAIN.
"""

from pathlib import Path
from datetime import datetime
import subprocess
import json
import csv

# Konfiguracja
BASE_DIR = Path.home() / "ICE_METROPOLIS"
PDF_DIR = BASE_DIR / "pdf_reports"
LOG_DIR = BASE_DIR / "logs"
CHAIN_FILE = LOG_DIR / "ICE_CHAIN_BLOCK.csv"
CID_REGISTRY = LOG_DIR / "IPFS_REPORT_LOG.csv"
KIDDUSH_LOG = LOG_DIR / "ICE_KIDDUSH_LOG.json"

for d in (PDF_DIR, LOG_DIR):
    d.mkdir(parents=True, exist_ok=True)

def kiddush_log(action: str, info: str):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "action": action,
        "info": info,
        "intention": "L'shem Shamayim – dla dobra i sprawiedliwości"
    }
    with open(KIDDUSH_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    print(f"🕊️ {action}: {info}")

def get_latest_pdf():
    pdfs = sorted(PDF_DIR.glob("ICE_ETHICS_REPORT_*.pdf"))
    return pdfs[-1] if pdfs else None

def ipfs_add(file_path: Path):
    cmd = ["ipfs", "add", "-Q", str(file_path)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    return result.stdout.strip()

def upload_latest_pdf():
    pdf = get_latest_pdf()
    if not pdf:
        print("❌ Brak pliku PDF do uploadu.")
        return

    kiddush_log("ipfs_upload_start", pdf.name)
    
    try:
        cid = ipfs_add(pdf)
        link = f"ipfs://{cid}"
        ts = datetime.now().isoformat()

        with open(CID_REGISTRY, "a", newline="", encoding="utf-8") as c:
            writer = csv.writer(c)
            writer.writerow([ts, pdf.name, cid, link])

        with open(CHAIN_FILE, "a", newline="", encoding="utf-8") as chain:
            writer = csv.writer(chain)
            writer.writerow([ts, "ETHICS_REPORT", pdf.name, cid])

        kiddush_log("ipfs_upload_success", cid)
        print(f"✅ Upload zakończony: {cid}")
        print(f"🔗 {link}")
        
    except Exception as e:
        kiddush_log("ipfs_upload_error", str(e))
        print(f"⚠️ Błąd uploadu: {e}")

if __name__ == "__main__":
    upload_latest_pdf()
