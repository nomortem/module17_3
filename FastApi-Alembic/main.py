from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from models import Product, Base, engine, Session


app = FastAPI()

# Создание таблиц, если они еще не созданы
Base.metadata.create_all(bind=engine)


@app.post("/products/")
def create_product(product: Product, db: Session = Session()):
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


@app.get("/products/{product_id}")
def read_product(product_id: int, db: Session = Session()):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
