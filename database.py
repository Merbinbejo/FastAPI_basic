from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_URL="postgresql://postgres:Prabhudhas%401@localhost:5432/Products"
engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)
