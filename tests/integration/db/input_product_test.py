from price_tracker.database.repositories import *

# Test the product is created in the database
product = Product(
    id=None,
    name="Test Product",
    url="https://example.com/test",
    retailer="Test Retailer",
    review_rating=2.5,
    review_count=5000
)

# Creates the product with the details above.
product_id = ProductRepo().addprod(product)