import os

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from ItemService import ItemService
import schemas, crud, models

app = FastAPI()
itemService = ItemService

def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/new")
def createNewItem(newItem: schemas.ItemBase, db: Session = Depends(get_db)):
    return crud.createItem(db, newItem)


@app.get("/items/{itemId}")
def getItemWithId(itemId: str):
    return {"message": itemId}


@app.get("/items")
async def getAllItems():
    return ItemService().getAllItems()

# https://fastapi.tiangolo.com/tutorial/path-params/
# https://packaging.python.org/en/latest/tutorials/packaging-projects/
