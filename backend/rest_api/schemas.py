from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    gold: int
    silver: int
    copper: int

class Item(ItemBase):
    id: int
    class Config:
        orm_mode = True


