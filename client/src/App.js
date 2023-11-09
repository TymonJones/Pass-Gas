import React from 'react';
import StationList from './components/StationList';
import './App.css'; // Add some CSS for styling

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
