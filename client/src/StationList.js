import React, { useEffect, useState } from 'react';
import Station from './Station';

const StationList = () => {
  const [stations, setStations] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/stations')
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        setStations(data);
        setIsLoading(false);
      })
      .catch(error => {
        setError(error);
        setIsLoading(false);
      });
  }, []);

  if (isLoading) return <div className="text-center mt-4 text-xl">Loading...</div>;
  if (error) return <div className="text-center text-red-500 mt-4 text-xl">Error: {error.message}</div>;

  return (
    <section className="container mx-auto p-4">
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {stations.length > 0 ? (
          stations.map(station => (
            <Station key={station.id} {...station} />
          ))
        ) : (
          <p className="text-center col-span-full">No stations available.</p>
        )}
      </div>
    </section>
  );
};

export default StationList;
