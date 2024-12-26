from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
# Инициализация экземпляра MetaData
metadata = MetaData()

Base = declarative_base()
engine = create_engine('sqlite:///./test.db')
Session = sessionmaker(bind=engine)

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Float)
    count = Column(Integer)
    description = Column(String)

    metadata = metadata
