from typing import List

from pydantic import BaseModel, Field

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
    item_id: list[int]


class Purchase(PurchaseBase):
    id: int

    class Config:
        orm_mode = True


class SaleBase(BaseModel):
    item_id: list[int]


class Sale(SaleBase):
    id: int

    class Config:
        orm_mode = True
