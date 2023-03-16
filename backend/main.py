from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
import schemas
from item_service import ItemService

app = FastAPI()
item_service = ItemService()


def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/items/new")
def createNewItem(newItem: schemas.ItemBase, db: Session = Depends(get_db)):
    return item_service.create_new_item(db, newItem)


@app.get("/items/{itemId}")
def getItemWithId(itemId: str, db: Session = Depends(get_db)):
    return item_service.get_item_by_id(db, itemId)


@app.get("/items")
async def getAllItems(db: Session = Depends(get_db)):
    return item_service.get_all_items(db)
