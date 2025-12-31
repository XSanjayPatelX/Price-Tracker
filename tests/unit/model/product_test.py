from price_tracker.models.product import Product

product = Product(
    id = None,
    name = "Test Product",
    url = "https://example.com/test",
    retailer = "Test Retailer",
    review_rating = None,
    review_count = None
)

print(product)