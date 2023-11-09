// StationCard.js
const StationCard = ({ name, address, price }) => {
    return (
      <div className="border p-4 rounded-lg shadow-md">
        <h2 className="text-xl font-bold">{name}</h2>
        <p>{address}</p>
        <p className="text-lg">{price}</p>
      </div>
    );
  };
  