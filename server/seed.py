from app import app, db
from models import GasStation

# Predefined list of gas stations
stations_data = [
    # ... your predefined stations
]

def seed_database():
    # Clear existing data
    db.drop_all()
    db.create_all()
    
    # Create new entries
    for station_data in stations_data:
        station = GasStation(
            name=station_data["name"],
            address=station_data["address"],
            latitude=station_data["latitude"],
            longitude=station_data["longitude"],
            gas_price=station_data["gas_price"]
        )
        db.session.add(station)
    
    # Commit changes
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():  # Push an application context for the database interactions
        seed_database()

