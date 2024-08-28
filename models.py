from pony.orm import Database, Required, PrimaryKey
from datetime import date

db = Database()

class Proizvod(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    date = Required(date)
    type = Required(str)
    expiration = Required(int)
    toBuy = Required(bool)

db.bind(provider='sqlite', filename='proizvodi.sqlite', create_db=True)
db.generate_mapping(create_tables=True)