from pony.orm import db_session
from datetime import date
from models import Proizvod

@db_session
def add_products():
    Proizvod.select().delete(bulk=True)

    # Food products
    Proizvod(name="Milk", date=date(2024, 6, 1), type="food", expiration=7, toBuy=True)
    Proizvod(name="Bread", date=date(2024, 6, 1), type="food", expiration=3, toBuy=True)
    Proizvod(name="Cheese", date=date(2024, 6, 1), type="food", expiration=30, toBuy=True)
    Proizvod(name="Apples", date=date(2024, 6, 1), type="food", expiration=14, toBuy=False)
    Proizvod(name="Chicken Breast", date=date(2024, 6, 1), type="food", expiration=5, toBuy=True)
    
    # Cleaning products
    Proizvod(name="Dish Soap", date=date(2024, 6, 1), type="cleaning", expiration=365, toBuy=True)
    Proizvod(name="Laundry Detergent", date=date(2024, 6, 1), type="cleaning", expiration=730, toBuy=True)
    Proizvod(name="Glass Cleaner", date=date(2024, 6, 1), type="cleaning", expiration=365, toBuy=False)
    Proizvod(name="All-Purpose Cleaner", date=date(2024, 6, 1), type="cleaning", expiration=365, toBuy=True)
    Proizvod(name="Bleach", date=date(2024, 6, 6), type="cleaning", expiration=730, toBuy=False)
    
    # Hygiene products
    Proizvod(name="Toothpaste", date=date(2024, 6, 6), type="hygiene", expiration=730, toBuy=True)
    Proizvod(name="Shampoo", date=date(2024, 6, 6), type="hygiene", expiration=365, toBuy=True)
    Proizvod(name="Body Wash", date=date(2024, 6, 21), type="hygiene", expiration=365, toBuy=False)
    Proizvod(name="Deodorant", date=date(2024, 6, 21), type="hygiene", expiration=365, toBuy=True)
    Proizvod(name="Hand Soap", date=date(2024, 6, 21), type="hygiene", expiration=365, toBuy=True)

add_products()