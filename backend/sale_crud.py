from sqlalchemy.orm import Session

import models
import schemas


def find_all_sales(db: Session):
    return db.query(models.Sale).all()


def get_sale_by_id(db: Session, sale_id: int):
    return db.query(models.Sale).filter(models.Sale.id == sale_id).first()


def create_item(db: Session, sale: schemas.SaleBase):
    sale_to_create = models.Sale(items=sale.items)
    db.add(sale_to_create)
    db.commit()
    db.refresh(sale_to_create)
    return sale_to_create
