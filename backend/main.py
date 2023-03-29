from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

import item_service
import models
import schemas
from purchase_service import PurchaseService
from sale_service import SaleService

app = FastAPI()
purchase_service = PurchaseService()
sale_service = SaleService()
item_service = item_service.ItemService()


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
        raise HTTPException(status_code=501, detail="Item not found")
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=success.id)


@app.get("/items/{itemId}")
async def getItemWithId(itemId: int, db: Session = Depends(get_db)) -> schemas.Item:
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
        raise HTTPException(status_code=501, detail="Item not found")
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=success.id)

@app.get("/purchase/{purchaseId}")
async def getPurchaseWithId(purchaseId: int, db: Session = Depends(get_db)) -> schemas.Purchase:
    purchase = purchase_service.get_purchase_by_id(db, purchaseId)
    if purchase is None:
        raise HTTPException(status_code=501, detail="Item not found")
    return purchase

@app.get("/sale")
async def get_all_sales(db: Session = Depends(get_db)):
    return sale_service.get_all_sales(db)


@app.post("/sale/new")
async def create_new_sale(new_sale: schemas.SaleBase, db: Session = Depends(get_db)):
    success = sale_service.create_new_sale(db, new_sale)
    if success == 0:
        raise HTTPException(status_code=501, detail="Item not found")
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=success.id)
