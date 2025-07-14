from DZpython1.price_list.database import Session, create_db
from DZpython1.price_list.car_model import Car


def car_database():
    create_db()
    session = Session()

    cars_data = [
        {"car_brand": "Audi", "model": "TT", "manufacturer": "Germany", "power": 320},
        {"car_brand": "Volkswagen", "model": "Touareg", "manufacturer": "Germany", "power": 270},
        {"car_brand": "Lisan", "model": "L9", "manufacturer": "China", "power": 449},
        {"car_brand": "Kia", "model": "Sportage", "manufacturer": "Korea", "power": 175},
        {"car_brand": "Mini", "model": "Cooper", "manufacturer": "Great Britain", "power": 184}
    ]

    for car in cars_data:
        session.add(Car(**car))

    session.commit()
    session.close()
