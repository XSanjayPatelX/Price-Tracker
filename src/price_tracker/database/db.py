import sqlite3
from pathlib import Path

DB_PATH = Path("data/processed/price_tracker.db")         # Database location

# Checks for .db file and ensures connection
def connect_db():
    d_path = DB_PATH.parent
    d_path_exists = d_path.exists()
    if d_path_exists is False:
        try:
            d_path.mkdir(
                parents = True,
                exist_ok = False
            )
        except FileExistsError:
            pass

    return sqlite3.connect(DB_PATH)

# Creates tables for database
def tables():
    con = connect_db()
    cursor = con.cursor()

    # Products table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            url TEXT NOT NULL,
            retailer TEXT NOT NULL,
            review_rating REAL,
            review_count INTEGER
        )
    """)

    # Price Tracker table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS price_tracker (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            collected_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            current_price REAL NOT NULL,
            original_price REAL,
            percentage_off INTEGER,
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    """)

    con.commit()
    con.close()

# test run - Ensures it creates a .db file in the data directory
#tables()