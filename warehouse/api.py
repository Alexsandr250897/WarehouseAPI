from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from warehouse import schemas, methods
from .database import get_db

router = APIRouter()

# Маршруты для продуктов
@router.get("/products/", response_model=list[schemas.Product])
def read_products(db: Session = Depends(get_db)):
    products = methods.get_products(db)
    if not products:
        raise HTTPException(status_code=404, detail="Products not found")
    return products

@router.get("/products/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = methods.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return methods.create_product(db, product)

@router.put("/products/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, updated_product: schemas.ProductCreate, db: Session = Depends(get_db)):
    product = methods.update_product(db, product_id, updated_product)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = methods.delete_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"detail": "Product deleted successfully"}

# Маршруты для заказов
@router.post("/orders/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    # Проверка наличия товаров на складе перед созданием заказа
    for item in order.items:
        product = methods.get_product(db, item.product_id)
        if not product:
            raise HTTPException(status_code=404, detail=f"Product with ID {item.product_id} not found")
        if product.quantity < item.quantity:
            raise HTTPException(status_code=400, detail=f"Not enough quantity for product {product.name}")

    return methods.create_order(db, order)
