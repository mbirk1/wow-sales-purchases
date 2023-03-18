from typing import List, Type

from sqlalchemy.orm import Session

import models
import schemas
from models import Purchase


def find_all_purchases(db: Session):
    return db.query(models.Purchase).all()


def get_purchases_by_id(db: Session, purchase_id: int):
    return db.query(models.Purchase).filter(models.Purchase.id == purchase_id).first()


def create_purchase(db: Session, purchase: schemas.PurchaseBase) -> int:
    purchase_to_create = models.Purchase(items=purchase.items)
    db.add(purchase_to_create)
    db.commit()
    db.refresh(purchase_to_create)
    return purchase_to_create


def find_all_purchases(db: Session) -> list[Type[Purchase]]:
    return db.query(models.Purchase).all()
