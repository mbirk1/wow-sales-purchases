from typing import Any

from sqlalchemy.orm import Session

import models
import schemas


def find_all_items(db: Session):
    return db.query(models.Item).all()


def get_item_by_id(db: Session, itemId: int):
    return db.query(models.Item).filter(models.Item.id == itemId).first()


def createItem(db: Session, item: schemas.ItemBase):
    itemToCreate = models.Item(name=item.name, gold=item.gold, silver=item.silver, copper=item.copper)
    db.add(itemToCreate)
    db.commit()
    db.refresh(itemToCreate)
    return itemToCreate
