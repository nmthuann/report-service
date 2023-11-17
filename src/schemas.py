from enum import Enum

from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class BaseSchema(BaseModel):
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]

class OrderSchema(BaseModel):
    order_id: int
    total_price: int
    status: str
    delivery_address: Optional[str]
    contact: Optional[str]
    discount_id: Optional[int]
    user_id: Optional[int]
    employee_id: Optional[int]
    shipping_id: Optional[int]
    payment_id: Optional[int]

class PaymentSchema(BaseModel):
    payment_id: int
    payment_name: str
    description: str

class DiscountSchema(BaseModel):
    discount_id: int
    description: str
    expired: datetime
    percent: int

class ShippingSchema(BaseModel):
    shipping_id: int
    shipping_name: str
    ship_cost: float
    estimated_time: int

class UserSchema(BaseModel):
    user_id: int
    first_name: str
    last_name: Optional[str]
    avatar_url: Optional[str]
    gender: Optional[str]
    birthday: datetime
    address: Optional[str]
    phone: str

class EmployeeSchema(BaseModel):
    employee_id: str
    salary: int
    work_status: bool
    position_id: Optional[int]

class PositionSchema(BaseModel):
    position_id: int
    position_name: str
    offer: float

class RoleEnum(str, Enum):
    User = 'User'
    Admin = 'Admin'

class AccountSchema(BaseModel):
    email: str
    password: str
    status: bool
    refresh_token: Optional[str]
    role: RoleEnum

class CategorySchema(BaseModel):
    category_id: int
    category_name: str
    description: Optional[str]
    category_url: Optional[str]

class ImageSchema(BaseModel):
    image_id: str
    product_id: Optional[int]
    url: str

class ProductSchema(BaseModel):
    product_id: int
    model_name: str
    vote: int
    price: int
    unit_price: int
    quantity: int
    status: bool
    description: Optional[str]
    operation_system: str
    hardware: str
    warranty_time: int
    category_id: Optional[int]
    discount_id: Optional[int]
    color: str
    battery: int
    screen: float
    memory: int
    front_camera: int
    behind_camera: int
    ram: int