from price_tracker.database.db import tables

def main():
    print("Price Tracker Started...")

    tables()
    print("Creating database tables...")

if __name__ == "__main__":
    main()