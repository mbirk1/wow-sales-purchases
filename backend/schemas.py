from typing import List

from pydantic import BaseModel

from models import Sale, Purchase


class ItemBase(BaseModel):
    name: str
    gold: int
    silver: int
    copper: int


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True


class PurchaseBase(BaseModel):
    items: List[Item]


class Purchase(PurchaseBase):
    id: int

    class Config:
        orm_mode = True


class SaleBase(BaseModel):
    items: List[Item]


class Sale(SaleBase):
    id: int

    class Config:
        orm_mode = True
