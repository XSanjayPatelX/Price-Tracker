from dataclasses import dataclass
import datetime
from typing import Optional

@dataclass
class PriceHistory:
    # Default
    id: Optional[int]           # Primary key
    product_id: int         # Foreign key
    collected_at: datetime.datetime

    # Pricing
    current_price: float           # Price of product, whether on sale or not
    original_price: Optional[float] | None   # Original price if on sale
    percentage_off: Optional[int] | None     # Percentage off product