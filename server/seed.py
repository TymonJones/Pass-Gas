from faker import Faker
from app import app, db
from models import GasStation

fake = Faker()

def seed_database(num_entries=10):
    # Clear existing data
    db.drop_all()
    db.create_all()

    # Create new entries
    for _ in range(num_entries):
        station = GasStation(
            name=fake.company(),
            address=fake.address(),
            latitude=fake.latitude(),
            longitude=fake.longitude(),
            gas_price=round(fake.random_number(digits=2) + fake.random_number(digits=2) / 100, 2)
        )
        db.session.add(station)

    # Commit changes
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        seed_database(20)  # Seed the database with 20 random gas stations


