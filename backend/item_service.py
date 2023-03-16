from sqlalchemy.orm import Session

import crud
from models import Item
from schemas import ItemBase


class ItemService:
    pass

    def create_new_item(self, db: Session, item: ItemBase):
        if self.validate(item):
            return crud.createItem(db, item)

    def validate(self, item: Item) -> bool:
        if item.gold is None or item.silver is None or item.copper is None or item.name is None:
            return False
        else:
            return True

    def get_all_items(self, db: Session) -> str:
        return crud.find_all_items(db)

    def get_item_by_id(self, db: Session, item_id: str):
        return crud.get_item_by_id(db, item_id)
