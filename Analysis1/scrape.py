import sqlite3
import time
import json
import requests

item_list = [
    "DIAMOND",
    "REDSTONE",
    "MAGIC_MUSHROOM_SOUP",
    "VIAL_OF_VENOM",
    "SALT_CUBE",
    "DIAMONITE",
    "ESSENCE_WITHER",
    "ESSENCE_CRIMSON",
]

with sqlite3.connect("skyblock-1.db") as conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            timestamp TEXT,
            item TEXT,
            buy_price REAL,
            sell_price REAL
        )
    """)
    for i in item_list:
        time.sleep(4)
        _ = requests.get(f"https://sky.coflnet.com/api/bazaar/{i}/history?start=2025-09-20&end=2026-03-20")
        j = json.loads(_.text)
        for k in j:
            if not "buy" in k.keys(): continue
            if not "sell" in k.keys(): continue
            conn.execute(
                "INSERT INTO prices (timestamp, item, buy_price, sell_price) VALUES (?, ?, ?, ?)",
                (k["timestamp"], i, k["buy"], k["sell"])
            )
    conn.commit()

print(f"Done. Scraped {len(item_list)} items.")
