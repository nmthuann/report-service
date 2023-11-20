from datetime import datetime

from src.models import OrderEntity


from typing import Optional
from pydantic import BaseModel
from src.models import OrderEntity

class OrderResponse(BaseModel):
    order_id: int
    total_price: int
    status: str
    delivery_address: Optional[str]
    contact: Optional[str]
    created_at: Optional[datetime]
    # Include other fields from OrderEntity that you want to expose

    # Reference fields
    discount_id: Optional[int]
    payment_id: Optional[int]
    user_id: Optional[int]
    employee_id: Optional[int]
    shipping_id: Optional[int]


    class Config:
        orm_mode = True
