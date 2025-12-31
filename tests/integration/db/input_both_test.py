from datetime import datetime

from price_tracker.database.repositories import ProductRepo, PriceHistoryRepo
from price_tracker.models.product import Product
from price_tracker.models.price_history import PriceHistory

product_repo = ProductRepo()
price_repo = PriceHistoryRepo()

product = Product(
    id = None,
    name = "Test Gaming Mouse",
    url = "https://amazon.co.uk/test-mouse",
    retailer = "amazon",
    review_rating = 4.6,
    review_count = 1200
)

product_id = product_repo.addprod(product)

price_entry = PriceHistory(
    id = None,
    product_id = product_id,
    collected_at = datetime.now(),
    current_price = 50.99,
    original_price = 70.99,
    percentage_off = 15
)

price_repo.addpricetrack(price_entry)

print("Price history inserted successfully")
