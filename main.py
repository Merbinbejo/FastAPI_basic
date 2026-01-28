from database import SessionLocal,engine
from models import Product
import database_model
from sqlalchemy.orm import Session
from fastapi import Depends,FastAPI
import models
from schema import ProductCreate

app=FastAPI()

database_model.Base.metadata.create_all(bind=engine)


products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    db=SessionLocal()

    try:
        count=db.query(Product).count
        if count==0:
            db.add_all(products)
            db.commit()
    finally:
        db.close()

if __name__=="__main__":
    init_db()

@app.get("/product")
def get_all(db:Session=Depends(get_db)):
    db_products=db.query(Product).all()
    return db_products

@app.get("/products/{id}")
def get_data(id:int,db:Session=Depends(get_db)):
    db_product=db.query(Product).filter(Product.id==id).first()
    if db_product:
        return db_product
    else:
        return "Data Not Found" 
    
@app.post("/products")
def add_product(products:ProductCreate,db:Session=Depends(get_db)):
    db_product = models.Product(**products.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)  # get auto-generated id

    return db_product

@app.put("/product/{id}")
def update_product(id:int,products:ProductCreate,db:Session=Depends(get_db)):
    db_products=db.query(Product).filter(Product.id==id).first()
    if db_products:
        db_products.id=products.id
        db_products.name=products.name
        db_products.description=products.description
        db_products.price=products.price
        db_products.quantity=products.quantity
        db.commit()
        return "Updated Successful"
    else:
        return "Data Not Found"

@app.delete("/product")
def delete_product(id:int,db:Session=Depends(get_db)):
    db_product=db.query(Product).filter(Product.id==id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Data Deleted"
    return"data not found"

