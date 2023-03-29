from typing import Type

from sqlalchemy.orm import Session

import item_crud
from models import Item
from schemas import ItemBase

class ItemService():
    pass
    def create_new_item(self, db: Session, item: ItemBase):
        if self.validate(item):
            return item_crud.create_item(db, item)


    def validate(self, item: ItemBase) -> bool:
        if item.gold is None or item.silver is None or item.copper is None or item.name is None:
            return False
        else:
            return True


    def get_all_items(self, db: Session) -> list[Type[Item]]:
        return item_crud.find_all_items(db)


    def get_item_by_id(self, db: Session, item_id: int):
        return item_crud.get_item_by_id(db, item_id)


    def get_items_from_purchase(self, db: Session, purchase_id: int):
        return item_crud.get_item_by_purchase_id(purchase_id, db)

    def get_items_from_sale(self, db: Session, sale_id: int):
        return item_crud.get_item_by_sale_id(sale_id, db)