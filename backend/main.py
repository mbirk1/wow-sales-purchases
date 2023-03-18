from http.client import HTTPResponse

from fastapi import FastAPI, Depends, HTTPException,status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

import models
import schemas
from purchase_service import PurchaseService
from item_service import ItemService

app = FastAPI()
item_service = ItemService()
purchase_service = PurchaseService()


def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/items/new")
async def createNewItem(newItem: schemas.ItemBase, db: Session = Depends(get_db)):
    success = item_service.create_new_item(db, newItem)
    if success == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=success)


@app.get("/items/{itemId}")
async def getItemWithId(itemId: str, db: Session = Depends(get_db)) -> schemas.Item:
    if item_service.get_item_by_id(db, itemId) is None:
        raise HTTPException(status_code=501, detail="Item not found")
    return item_service.get_item_by_id(db, itemId)


@app.get("/items")
async def getAllItems(db: Session = Depends(get_db)):
    return item_service.get_all_items(db)

@app.get("/purchases")
async def get_all_purchases(db: Session = Depends(get_db)):
    return purchase_service.get_all_purchases(db)

@app.post("/purchases/new")
async def create_new_purchase(new_purchase: schemas.PurchaseBase, db: Session = Depends(get_db)):
    success = purchase_service.create_new_purchase(db, new_purchase)
    if success == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=success)