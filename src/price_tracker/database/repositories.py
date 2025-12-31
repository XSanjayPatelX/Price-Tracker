from price_tracker.database.db import connect_db
from price_tracker.models.product import Product
from price_tracker.models.price_history import PriceHistory

# Collect product object
class ProductRepo():
    def addprod(self, product: Product) -> int:
        # Check for already existing product
        existing_prod = self.collect_url(product.url)
        if existing_prod is not None:
            print("The product already exists:", 
                  "ID:", int(existing_prod.id), 
                  "-", existing_prod.name
            )
            
            return existing_prod.id

        con = connect_db()
        cursor = con.cursor()

        cursor.execute("""
            INSERT INTO products (
                name, url, retailer, review_rating, review_count
                )
                VALUES (?, ?, ?, ?, ?)
            """, (
                product.name,
                product.url,
                product.retailer,
                product.review_rating,
                product.review_count
        ))

        con.commit()
        product_id = cursor.lastrowid           # Generates ID and retrieves it for Python
        con.close()

        return product_id

    # Checks for repeated URLs
    def collect_url(self, url: str) -> Product:
        con = connect_db()
        cursor = con.cursor()

        cursor.execute("""
            SELECT id, name, url, retailer, review_rating, review_count
            FROM products
            WHERE url = ?
        """, (url,))

        row = cursor.fetchone()         # Returns only one row/entry
        con.close()

        if row is None:
            return None

        return Product(
            id=row[0],
            name=row[1],
            url=row[2],
            retailer=row[3],
            review_rating=row[4],
            review_count=row[5]
        )

# Stores price into history
class PriceHistoryRepo:
    def addpricetrack(self, entry: PriceHistory) -> None:
        con = connect_db()
        cursor = con.cursor()

        cursor.execute("""
            INSERT INTO price_tracker (
                product_id,
                collected_at,
                current_price,
                original_price,
                percentage_off
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            entry.product_id,
            entry.collected_at.strftime("%Y-%m-%d %H:%M:%S"),
            entry.current_price,
            entry.original_price,
            entry.percentage_off
        ))

        con.commit()
        con.close()
