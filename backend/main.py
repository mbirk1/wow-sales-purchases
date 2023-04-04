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


@app.get("/items")
async def getAllItems(db: Session = Depends(get_db)):
    return item_service.get_all_items(db)


@app.post("/items/new")
async def createNewItem(new_item: schemas.ItemBase, db: Session = Depends(get_db)):
    success = item_service.create_new_item(db, new_item)
    if success == 0:
        raise HTTPException(status_code=501, detail="Item not found")
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=success.id)


@app.get("/items/{itemId}")
async def getItemWithId(item_id: int, db: Session = Depends(get_db)) -> schemas.Item:
    item = item_service.get_item_by_id(db, item_id)
    if item is None:
        raise HTTPException(status_code=501, detail="Item not found")
    return item

@app.get("/items/highest/{id}")
async def get_item_from_name_with_highest_price(name: str, db: Session = Depends(get_db)) -> schemas.Item:
    item = item_service.get_item_from_name_highest_price(name, db)
    if item is None:
        raise HTTPException(status_code=501, detail="Item not found")
    return item

@app.get("/items/lowest/{name}")
async def get_item_from_name_with_lowest_price(name: str, db: Session = Depends(get_db)) -> schemas.Item:
    item = item_service.get_item_from_name_lowest_price(name, db)
    if item is None:
        raise HTTPException(status_code=501, detail="Item not found")
    return item


@app.get("/purchases")
async def get_all_purchases(db: Session = Depends(get_db)):
    return purchase_service.get_all_purchases(db)


@app.post("/purchases/new")
async def create_new_purchase(new_purchase: schemas.PurchaseBase, db: Session = Depends(get_db)):
    success = purchase_service.create_new_purchase(db, new_purchase)
    if success == 0:
        raise HTTPException(status_code=501, detail="Purchase not found")
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=success.id)


@app.get("/purchase/{purchaseId}")
async def get_purchase_from_id(purchase_id: int, db: Session = Depends(get_db)) -> schemas.Purchase:
    purchase = purchase_service.get_purchase_by_id(db, purchase_id)
    if purchase is None:
        raise HTTPException(status_code=501, detail="Purchase not found")
    return purchase


@app.get("/sale")
async def get_all_sales(db: Session = Depends(get_db)):
    return sale_service.get_all_sales(db)


@app.post("/sale/new")
async def create_new_sale(new_sale: schemas.SaleBase, db: Session = Depends(get_db)):
    success = sale_service.create_new_sale(db, new_sale)
    if success == 0:
        raise HTTPException(status_code=501, detail="Sale not found")
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=success.id)


@app.get("/sale/{saleId}")
async def get_sale_by_id(sale_id: int, db: Session = Depends(get_db)) -> schemas.Purchase:
    sale = sale_service.get_sale_by_id(sale_id, db)
    if sale is None:
        raise HTTPException(status_code=501, detail="Sale not found")
    return sale