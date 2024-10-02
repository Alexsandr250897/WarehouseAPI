from pydantic import BaseModel
from datetime import datetime

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

class OrderItemBase(BaseModel):
    product_id: int
    quantity: int

class OrderItemCreate(OrderItemBase):
    pass

class OrderItem(OrderItemBase):
    id: int

    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    status: str

class OrderCreate(OrderBase):
    items: list[OrderItemCreate]

class Order(OrderBase):
    id: int
    created_at: datetime
    items: list[OrderItem]

    class Config:
        orm_mode = True
