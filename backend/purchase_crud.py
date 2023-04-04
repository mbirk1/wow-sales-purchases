from typing import Type

from sqlalchemy import text
from sqlalchemy.orm import Session

import models
import schemas


def find_all_purchases(db: Session) -> list[Type[models.Purchase]]:
    return db.query(models.Purchase).all()


def get_purchases_by_id(db: Session, purchase_id: int) -> models.Purchase:
    return db.query(models.Purchase).filter(models.Purchase.id == purchase_id).first()


def create_purchase(db: Session, purchase: schemas.PurchaseBase) -> models.Purchase:
    purchase_model = models.Purchase()
    db.add(purchase_model)
    db.commit()
    db.refresh(purchase_model)
    for item in purchase.items:
        purchase_item = text(
            "INSERT INTO tab_api_purchase_items (purchase_id, item_id) VALUES (" + str(purchase_model.id) + "," + item + ")")
        db.execute(purchase_item)
        db.commit()
    return purchase_model
