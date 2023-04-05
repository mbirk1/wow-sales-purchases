from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    name: str = Field(title="Name of the Item")
    gold: int = Field(title="Gold value")
    silver: int= Field(title="Silver value")
    copper: int = Field(title="Copper value")


class Item(ItemBase):
    id: int = Field(title="Unique identifier of the Item")

    class Config:
        orm_mode = True


class PurchaseBase(BaseModel):
    item_id: list[int] = Field(title="Items in Purchase")


class Purchase(PurchaseBase):
    id: int= Field(title="Unique identifier of the purchase")

    class Config:
        orm_mode = True


class SaleBase(BaseModel):
    item_id: list[int]= Field(title="Items in Sale")


class Sale(SaleBase):
    id: int= Field(title="Unique identifier of the sale")

    class Config:
        orm_mode = True
