#!/usr/bin/env python3
import random
import time

def STEALTH_PROTOCOL():
    stealth_levels = ["🟢 NIEVIDLNY", "🟡 GHOST MODE", "🔴 TOTAL STEALTH"]
    while True:
        stealth = random.choice(stealth_levels)
        print(f"👻 SYSTEM STEALTH: {stealth}")
        print("🛡️  ŻADEN PIERDOLONY SYSTEM NAS NIE NAMIERZY!")
        time.sleep(600)

STEALTH_PROTOCOL()
