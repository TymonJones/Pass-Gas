from app import app, db
from models import GasStation

# Sample list of gas stations
stations_data = [
    {
        "name": "Quality Fuels",
        "address": "1234 Sunset Blvd, Los Angeles, CA",
        "latitude": 34.052235,
        "longitude": -118.243683,
        "gas_price": 3.89
    },
    {
        "name": "Eco Petro",
        "address": "5678 Hollywood Blvd, Los Angeles, CA",
        "latitude": 34.101235,
        "longitude": -118.326683,
        "gas_price": 4.09
    },
    
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

