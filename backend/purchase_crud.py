from typing import Type

from sqlalchemy.orm import Session

import models
import schemas


def find_all_purchases(db: Session) -> list[Type[models.Purchase]]:
    return db.query(models.Purchase).all()


def get_purchases_by_id(db: Session, purchase_id: int):
    return None


def create_purchase(db: Session, purchase: schemas.PurchaseBase):
    purchase_to_create = models.Purchase()

    return None
