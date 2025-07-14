from DZpython1.price_list.database import Base
from sqlalchemy import Column, Integer, String


class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    car_brand = Column(String(100), nullable=False)
    model = Column(String(50), nullable=False)
    manufacturer = Column(String(50), nullable=False)
    power = Column(Integer)





