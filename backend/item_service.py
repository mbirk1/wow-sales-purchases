import math
from typing import Type

from sqlalchemy.orm import Session

import item_crud
import models
import schemas


class ItemService:
    pass

    def create_new_item(self, db: Session, item: schemas.ItemBase):
        self.adjustPrice(item)
        if self.validateNonNull(item):
            return item_crud.create_item(db, item)

    def validateNonNull(self, item: schemas.ItemBase) -> bool:
        if item.gold is None or item.silver is None or item.copper is None or item.name is None:
            return False
        else:
            return True

    def adjustPrice(self, item: schemas.ItemBase) -> schemas.ItemBase:
        copper = item.copper * 0.01
        copper = math.trunc(copper)
        if copper > 0:
            item.copper = item.copper - (copper * 100)
            item.silver = item.silver + copper

        silver = item.silver * 0.01
        silver = math.trunc(silver)
        if copper > 0:
            item.silver = item.silver - (silver * 100)
            item.gold = item.gold + silver
        return item

    def get_all_items(self, db: Session) -> list[Type[models.Item]]:
        return item_crud.find_all_items(db)

    def get_item_by_id(self, db: Session, item_id: int):
        return item_crud.get_item_by_id(db, item_id)

    def get_items_from_purchase(self, db: Session, purchase_id: int):
        return item_crud.get_item_by_purchase_id(purchase_id, db)

    def get_items_from_sale(self, db: Session, sale_id: int):
        return item_crud.get_item_by_sale_id(sale_id, db)

    def get_item_from_name_highest_price(self, name: str, db: Session):
        items = item_crud.get_item_by_name(name, db)
        id = 0
        for item in items:
            if (self.price_is_higher(item, id, db)):
                id = item.id
        return self.convert_model_to_schema(self.get_item_by_id(db, id)).dict()

    def get_item_from_name_lowest_price(self, name: str, db: Session):
        items = item_crud.get_item_by_name(name, db)
        id = 0
        count = 0
        for item in items:
            count = count + 1
            if (self.price_is_lower(item, id, db)):
                id = item.id
        return self.convert_model_to_schema(self.get_item_by_id(db, id)).dict()

    def convert_model_to_schema(self, item_model: models.Item) -> schemas.Item:
        schema = schemas.Item(id=item_model.id, gold=item_model.gold, silver=item_model.silver,
                              copper=item_model.copper, name=item_model.name)
        return schema

    def price_is_higher(self, item: Type[models.Item], id: int, db: Session):
        if id != 0:
            highest_item = self.get_item_by_id(db, id)
            if item.gold > highest_item.gold:
                return True
            if item.silver > highest_item.silver and item.gold == highest_item.gold:
                return True
            if item.copper > highest_item.copper and item.silver == highest_item.silver and item.gold == highest_item.gold:
                return True
        else:
            return True

    def price_is_lower(self, item: Type[models.Item], id: int, db: Session):
        if id != 0:
            lowest_item = self.get_item_by_id(db, id)
            if item.gold < lowest_item.gold:
                return True
            if item.silver < lowest_item.silver and item.gold == lowest_item.gold:
                print("silver")
                return True
            if item.copper < lowest_item.copper and item.silver == lowest_item.silver and item.gold == lowest_item.gold:
                print("copper")
                return True
        else:
            return True
