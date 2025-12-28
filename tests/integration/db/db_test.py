import sqlite3
from pathlib import Path

DB_PATH = Path("tests/integration/db/data/processed/price_tracker_test.db")

def connect_db():
    directory_path = DB_PATH.parent
    directory_exists = directory_path.exists()
    if directory_exists is False:
        try:
            directory_path.mkdir(
                parents = True,
                exist_ok = False
            )
        except FileExistsError:
            pass

    return sqlite3.connect(DB_PATH)

def tables():
    con = connect_db()
    cursor = con.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS name_2 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS name_1 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)

    con.commit()
    con.close()

# Create the tables - running the code above.
tables()