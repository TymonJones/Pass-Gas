import React from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';

const StationDetails = ({ station }) => {
  const { name, address, latitude, longitude, gas_price } = station;

  return (
    <div className="container mx-auto mt-4 p-4 bg-white shadow rounded-lg">
      <h2 className="text-2xl font-bold text-gray-800">{name}</h2>
      <p className="text-md text-gray-600 mt-2">{address}</p>
      <div className="my-3">
        <h3 className="text-lg text-gray-700">Location:</h3>
        <p className="text-md text-gray-500">Latitude: {latitude}</p>
        <p className="text-md text-gray-500">Longitude: {longitude}</p>
      </div>
      <div className="my-3">
        <h3 className="text-lg text-gray-700">Pricing:</h3>
        <p className="text-md font-semibold text-gray-800">${gas_price}</p>
      </div>
      {/* Map view */}
      <div className="h-64">
        <MapContainer center={[latitude, longitude]} zoom={13} scrollWheelZoom={false} className="h-full">
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          />
          <Marker position={[latitude, longitude]}>
            <Popup>{name}</Popup>
          </Marker>
        </MapContainer>
      </div>
    </div>
  );
};

export default StationDetails;
