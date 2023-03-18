from typing import List, Type

from sqlalchemy.orm import Session

import models
import schemas
from models import Item


def find_all_items(db: Session) -> list[Type[Item]]:
    return db.query(models.Item).all()


def get_item_by_id(db: Session, item_id: int) -> Type[models.Item] | None:
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def create_item(db: Session, item: schemas.ItemBase):
    item_to_create = models.Item(name=item.name, gold=item.gold, silver=item.silver, copper=item.copper)
    db.add(item_to_create)
    db.commit()
    db.refresh(item_to_create)
    return item_to_create
