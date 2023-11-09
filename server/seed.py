from app import app
from models import db, GasStation

def seed():
    # Delete existing data
    db.drop_all()
    db.create_all()

    # Add seed data
    station1 = GasStation(name="Gas Station 1", address="123 LA Street", latitude=34.0522, longitude=-118.2437, gas_price=4.99)
    station2 = GasStation(name="Gas Station 2", address="456 LA Avenue", latitude=34.0522, longitude=-118.2437, gas_price=5.09)

    db.session.add(station1)
    db.session.add(station2)

    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        seed()
