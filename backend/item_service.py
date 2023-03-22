from typing import List, Type

from sqlalchemy.orm import Session

import item_crud
from models import Item
from schemas import ItemBase


def create_new_item(self, db: Session, item: ItemBase):
    if validate(item):
        return item_crud.create_item(db, item)


def validate(item: ItemBase) -> bool:
    if item.gold is None or item.silver is None or item.copper is None or item.name is None:
        return False
    else:
        return True


def get_all_items(db: Session) -> list[Type[Item]]:
    return item_crud.find_all_items(db)


def get_item_by_id(db: Session, item_id: int):
    return item_crud.get_item_by_id(db, item_id)


def get_items_from_purchase(db: Session, purchase_id: int):
    return item_crud.get_item_by_purchase_id(purchase_id, db)
