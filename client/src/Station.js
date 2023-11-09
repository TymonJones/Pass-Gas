import React from 'react';

const Station = ({ name, address, latitude, longitude, gas_price }) => {
  return (
    <article className="border border-gray-200 rounded-lg shadow-lg p-4 bg-white hover:bg-gray-50 transition-colors">
      <h2 className="text-lg font-bold text-gray-900">{name}</h2>
      <p className="text-gray-600">{address}</p>
      <div className="my-2">
        <p className="text-sm text-gray-500">Latitude: {latitude}</p>
        <p className="text-sm text-gray-500">Longitude: {longitude}</p>
      </div>
      <p className="text-md font-semibold text-gray-800">${gas_price}</p>
    </article>
  );
};

export default Station;
