from dataclasses import dataclass
import datetime

class PriceHistory:
    product_id: int
    price: float
    collected_at: datetime.datetime