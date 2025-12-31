from datetime import datetime

from price_tracker.database.repositories import PriceHistoryRepo
from price_tracker.models.price_history import PriceHistory

price_repo = PriceHistoryRepo()

price_entry = PriceHistory(
    id = None,
    product_id = 1,          # product_id - Should be going here, but for testing reasons, it wont for now
    collected_at = datetime.now(),
    current_price = 50.99,
    original_price = 70.99,
    percentage_off = 15
)

price_repo.addpricetrack(price_entry)

print("Price history inserted successfully")
