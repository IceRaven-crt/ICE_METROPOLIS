#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ICE_METROPOLIS · Ethics Report Module
Codzienny raport etyczny łączący dane finansowe z zasadami Maaser & Tikun.
"""

from datetime import datetime
from decimal import Decimal
from random import choice
from pathlib import Path
import json
import csv

# Konfiguracja
CONFIG = {
    "maaser_percent": Decimal("0.10"),
    "ethical_tags": ["education", "health", "renewable", "community", "peace"],
    "prohibited_tags": ["weapons", "speculation", "pollution"],
    "report_dir": Path.home() / "ICE_METROPOLIS" / "reports",
    "log_dir": Path.home() / "ICE_METROPOLIS" / "logs",
}

CONFIG["report_dir"].mkdir(parents=True, exist_ok=True)
CONFIG["log_dir"].mkdir(parents=True, exist_ok=True)

def calculate_maaser(total_profit: Decimal):
    maaser = total_profit * CONFIG["maaser_percent"]
    remainder = total_profit - maaser
    return maaser, remainder

def tikun_filter(portfolio):
    approved, rejected = [], []
    for asset in portfolio:
        tags = asset.get("tags", [])
        if any(tag in CONFIG["prohibited_tags"] for tag in tags):
            rejected.append(asset)
        else:
            approved.append(asset)
    return approved, rejected

def responsibility_index(roi_score: float, impact_ratio: float):
    index = (roi_score * 0.4) + (impact_ratio * 0.6)
    if index >= 0.9:
        grade = "HIGH"
    elif index >= 0.7:
        grade = "MEDIUM"
    else:
        grade = "LOW"
    return round(index, 2), grade

def kiddush_log(action: str, amount):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "action": action,
        "amount": str(amount),
        "intention": "L'shem Shamayim – dla dobra i sprawiedliwości",
    }
    path = CONFIG["log_dir"] / "ICE_KIDDUSH_LOG.json"
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
    return log_entry

def gratitude_phrase():
    phrases = [
        "Baruch Hashem, za każdy dzień pracy i światła.",
        "Z wdzięcznością za możliwość czynienia dobra poprzez technologię.",
        "Niech każdy zysk stanie się narzędziem Tikun Olam.",
        "Bogactwo to narzędzie, nie cel. Dziękujemy Hashem za mądrość.",
    ]
    return choice(phrases)

def generate_ethics_report(today_profit: Decimal, portfolio: list):
    maaser, rest = calculate_maaser(today_profit)
    approved, rejected = tikun_filter(portfolio)
    roi_score = float(rest / today_profit)
    impact_ratio = len(approved) / max(len(portfolio), 1)
    index, grade = responsibility_index(roi_score, impact_ratio)

    kiddush_log("maaser_transfer", maaser)
    kiddush_log("tikun_invest_filter", f"{len(approved)} ok / {len(rejected)} out")

    date_str = datetime.now().strftime("%Y-%m-%d_%H%M")
    report_path = CONFIG["report_dir"] / f"ICE_ETHICS_REPORT_{date_str}.txt"

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("🧊 ICE_METROPOLIS — ETHICAL IMPACT REPORT\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("────────────────────────────────────────────\n")
        f.write("🤍 ETHICAL IMPACT\n")
        f.write("────────────────────────────────────────────\n")
        f.write(f"Maaser (10%): ${maaser:,.2f} → Chesed & Shalom Funds\n")
        f.write(f"Approved Tikun investments: {len(approved)} / {len(portfolio)}\n")
        f.write(f"Rejected unethical assets: {len(rejected)}\n")
        f.write(f"Responsibility Index: {index} → {grade}\n")
        f.write("────────────────────────────────────────────\n")
        f.write("🕊️ GRATITUDE\n")
        f.write("────────────────────────────────────────────\n")
        f.write(gratitude_phrase() + "\n")
        f.write("────────────────────────────────────────────\n")
        f.write("📜 Signed: ICE_RAVEN_2137\n")

    csv_log = CONFIG["log_dir"] / "ETHICS_REPORT_LOG.csv"
    with open(csv_log, "a", newline="", encoding="utf-8") as c:
        writer = csv.writer(c)
        writer.writerow([datetime.utcnow().isoformat(), float(today_profit),
                         float(maaser), index, grade])

    print(f"✅ Raport etyczny zapisany: {report_path}")
    return report_path

if __name__ == "__main__":
    profit = Decimal("287800")
    sample_portfolio = [
        {"name": "Solar Future Fund", "tags": ["renewable", "education"]},
        {"name": "Peace Health Ventures", "tags": ["health", "community"]},
        {"name": "Specu Corp", "tags": ["speculation"]},
    ]
    generate_ethics_report(profit, sample_portfolio)
