from price_tracker.models.product import Product

product = Product(
    id=1,
    name="Test Product",
    url="https://example.com/test",
    retailer="Test Retailer",
    current_price=10.0,
    percentage_off=None,
    original_price=None,
    review_rating=None,
    review_count=None
)

print(product)