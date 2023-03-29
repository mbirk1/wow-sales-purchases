import json

from sqlalchemy.orm import Session

import item_service
import models
import purchase_crud
import schemas

service_item = item_service.ItemService()


def purchase_is_valid(purchase: schemas.PurchaseBase) -> bool:
    for item in purchase.items:
        if item == 0:
            return False
    return True


class PurchaseService:

    def create_new_purchase(self, db: Session, purchase: schemas.PurchaseBase):
        if purchase_is_valid(purchase):
            return purchase_crud.create_purchase(db, purchase)
        else:
            return 0

    def get_all_purchases(self, db: Session):
        purchases = purchase_crud.find_all_purchases(db)
        return_values = []
        for purchase in purchases:
            return_values.append(self.convert_model_to_schema(purchase, db))
        return return_values

    def get_purchase_by_id(self, db: Session, purchase_id: int) -> models.Purchase | None:
        model = purchase_crud.get_purchases_by_id(db, purchase_id)
        if model is not None:
            purchase = self.convert_model_to_schema(model, db)
            return purchase.dict()
        else:
            return None

    def convert_model_to_schema(self, purchase_model: models.Purchase, db: Session) -> schemas.Purchase:
        items = service_item.get_items_from_purchase(db, purchase_model.id)
        item_ids = []
        for item in items:
            item_ids.append(item.item_id)
        schema = schemas.Purchase(id=purchase_model.id, item_id=item_ids)
        return schema
