from sqlalchemy.orm import Session

import item_service
import models
import sale_crud
import schemas

service_item = item_service.ItemService()


def sale_is_valid(sale: schemas.SaleBase) -> bool:
    for item in sale.items:
        if item.id == 0:
            return False
    return True


class SaleService:
    pass

    def get_all_sales(self, db: Session):
        sales = sale_crud.find_all_sales(db)
        return_sales = []
        for sale in sales:
            return_sales.append(self.convert_model_to_schema(sale, db))

        return return_sales

    def create_new_sale(self, db: Session, sale: schemas.SaleBase):
        if (sale_is_valid(sale)):
            return sale_crud.create_item(db, sale)
        else:
            return 0

    def get_sale_by_id(self, db: Session, sale_id: int) -> models.Purchase | None:
        model = sale_crud.get_sale_by_id(db, sale_id)
        if model is not None:
            sale = self.convert_model_to_schema(model, db)
            return sale.dict()
        else:
            return None

    def convert_model_to_schema(self, sale_model: models.Sale, db: Session) -> schemas.Sale:
        items = service_item.get_items_from_sale(db, sale_model.id)
        item_ids = []
        for item in items:
            item_ids.append(item.item_id)
        schema = schemas.Purchase(id=sale_model.id, item_id=item_ids)
        return schema
