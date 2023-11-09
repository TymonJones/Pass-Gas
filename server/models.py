from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class GasStation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    address = db.Column(db.String(120))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    gas_price = db.Column(db.Float)

    def __init__(self, name, address, latitude, longitude, gas_price):
        self.name = name
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.gas_price = gas_price
