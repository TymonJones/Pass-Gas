from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from models import db, GasStation
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pass_gas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return "Welcome to Pass Gas!"

# Get all gas stations
@app.route('/stations', methods=['GET'])
def get_stations():
    stations = GasStation.query.all()
    return jsonify([station.to_json() for station in stations])

# Get a single gas station
@app.route('/stations/<int:id>', methods=['GET'])
def get_station(id):
    station = GasStation.query.get_or_404(id)
    return jsonify(station.to_json())

# Create a new gas station
@app.route('/stations', methods=['POST'])
def create_station():
    if not request.json or not 'name' in request.json:
        abort(400)
    station = GasStation(
        name=request.json['name'],
        address=request.json.get('address', ""),
        latitude=request.json.get('latitude', 0),
        longitude=request.json.get('longitude', 0),
        gas_price=request.json.get('gas_price', 0)
    )
    db.session.add(station)
    db.session.commit()
    return jsonify(station.to_json()), 201

# Update a gas station
@app.route('/stations/<int:id>', methods=['PUT'])
def update_station(id):
    station = GasStation.query.get_or_404(id)
    if not request.json:
        abort(400)
    station.name = request.json.get('name', station.name)
    station.address = request.json.get('address', station.address)
    station.latitude = request.json.get('latitude', station.latitude)
    station.longitude = request.json.get('longitude', station.longitude)
    station.gas_price = request.json.get('gas_price', station.gas_price)
    db.session.commit()
    return jsonify(station.to_json())

# Delete a gas station
@app.route('/stations/<int:id>', methods=['DELETE'])
def delete_station(id):
    station = GasStation.query.get_or_404(id)
    db.session.delete(station)
    db.session.commit()
    return jsonify({'result': True})

# Helper method to convert a GasStation to a JSON representation
def to_json(self):
    return {
        'id': self.id,
        'name': self.name,
        'address': self.address,
        'latitude': self.latitude,
        'longitude': self.longitude,
        'gas_price': self.gas_price
    }

GasStation.to_json = to_json

if __name__ == '__main__':
    app.run(debug=True)
