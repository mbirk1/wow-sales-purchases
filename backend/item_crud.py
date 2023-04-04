from typing import List, Type

from sqlalchemy import text
from sqlalchemy.orm import Session

import models
import schemas
from models import Item


def find_all_items(db: Session) -> list[Type[Item]]:
    return db.query(models.Item).all()


def get_item_by_id(db: Session, item_id: int) -> models.Item | None:
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def create_item(db: Session, item: schemas.ItemBase):
    item_to_create = models.Item(name=item.name, gold=item.gold, silver=item.silver, copper=item.copper)
    db.add(item_to_create)
    db.commit()
    db.refresh(item_to_create)
    return item_to_create


def get_item_by_purchase_id(purchase_id, db: Session) -> list[dict]:
    stmt = text(
        "SELECT * FROM tab_api_item as i INNER JOIN tab_api_purchase_items tapi on i.id = tapi.item_id WHERE " +
        "purchase_id =" + str(purchase_id))
    result = db.execute(stmt).all()
    return result

def get_item_by_sale_id(sale_id, db: Session) -> list[dict]:
    stmt = text(
        "SELECT * FROM tab_api_item as i INNER JOIN tab_api_sale_items tapi on i.id = tapi.item_id WHERE " +
        "sale_id =" + str(sale_id))
    result = db.execute(stmt).all()
    return result


def get_item_by_name(name: str, db:Session) -> list[Type[models.Item]]:
    result = db.query(models.Item).filter(Item.name.like("%"+name+"%"))
    return result