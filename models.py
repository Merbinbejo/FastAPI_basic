from database_model import Base
from sqlalchemy import Column,Integer,String,Float

class Product(Base):

    __tablename__="Products"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    description=Column(String)
    price=Column(Float)
    quantity=Column(Integer)