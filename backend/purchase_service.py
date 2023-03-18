from sqlalchemy.orm import Session

import purchase_crud
from schemas import PurchaseBase


def purchase_is_valid(purchase: PurchaseBase) -> bool:
    for item in purchase.items:
        if item.id == 0:
            return False
    return True


class PurchaseService:
    pass

    def create_new_purchase(self, db: Session, purchase: PurchaseBase):
        if purchase_is_valid(purchase):
            return purchase_crud.create_purchase(db, purchase)
        else:
            return 0

    def get_all_purchases(self, db: Session):
        return purchase_crud.find_all_purchases(db)
