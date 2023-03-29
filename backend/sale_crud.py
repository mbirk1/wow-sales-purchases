from typing import Type

from sqlalchemy import text
from sqlalchemy.orm import Session

import models
import schemas


def find_all_sales(db: Session) -> list[Type[models.Sale]]:
    return db.query(models.Sale).all()


def get_sale_by_id(db: Session, sale_id: int) -> Type[models.Sale] | None:
    return db.query(models.Sale).filter(models.Sale.id == sale_id).first()


def create_item(db: Session, sale: schemas.SaleBase) -> models.Sale:
    sale_model = models.Sale()
    db.add(sale_model)
    db.commit()
    db.refresh(sale_model)
    for item in sale.items:
        sale_item = text(
            "INSERT INTO tab_api_sale_items (sale_id, item_id) VALUES (" + str(sale_model.id) + "," + str(
                item.id) + ")")
        db.execute(sale_item)
        db.commit()
    return sale_model
