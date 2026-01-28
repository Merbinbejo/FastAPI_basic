from pydantic import BaseModel

class ProductCreate(BaseModel):
    id:int
    name: str
    description: str
    price: float
    quantity: int

class ProductResponse(ProductCreate):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2