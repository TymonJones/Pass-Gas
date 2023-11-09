import React from 'react';

const Station = ({ name, address, latitude, longitude, gas_price }) => {
  return (
    <article>
      <h2>{name}</h2>
      <p>{address}</p>
      <p>Coordinates: {latitude}, {longitude}</p>
      <p>Price: ${gas_price}</p>
    </article>
  );
};

export default Station;
