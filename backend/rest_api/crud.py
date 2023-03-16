from sqlalchemy.orm import Session
import models, schemas


def getAllItems(db: Session):
    return db.query(models.Item)


def createItem(db: Session, item: schemas.ItemBase):
    itemToCreate = models.Item(name=item.name, gold= item.gold, silver=item.silver, copper=item.copper)
    db.add(itemToCreate)
    db.commit()
    db.refresh(itemToCreate)
    return itemToCreate
