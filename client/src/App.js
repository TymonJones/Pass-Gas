import React from 'react';
import StationList from './StationList';
import Styling from './index.css'; // Add some CSS for styling
import Station from './Station.js'


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Pass Gas</h1>
      </header>
      <main>
        <StationList />
      </main>
    </div>
  );
}

export default App;
