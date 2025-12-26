from dataclasses import dataclass
from typing import Optional

@dataclass
class Product:
    # Default
    id: int
    name: str                      # Full name of the item
    url: str
    retailer: str                  # Retailer, for future cases
    
    # Pricing
    current_price: float           # Price of product, whether on sale or not
    percentage_off: Optional[int] | None     # Percentage off product
    original_price: Optional[float] | None   # Original price if on sale
    
    # Reviews
    review_rating: Optional[float] | None    # Rating, e.g. 4.5/5
    review_count: Optional[int] | None       # Count, e.g. 750