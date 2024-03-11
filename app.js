import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
    const [flights, setFlights] = useState([]);
  
    useEffect(() => {
      axios.get('http://localhost:5000/flights')
        .then(response => setFlights(response.data))
        .catch(error => console.error(error));
    }, []);
  
    const handleBookFlight = flightId => {
      axios.post('http://localhost:5000/book', { flightId })
        .then(response => console.log(response.data.message))
        .catch(error => console.error(error));
    };
  
    return (
      <div>
        <h1>Available Flights</h1>
        <ul className="flight-list">
          {flights.map(flight => (
            <li key={flight.id} className="flight-item">
              {flight.origin} to {flight.destination}
              <button className="book-button" onClick={() => handleBookFlight(flight.id)}>Book</button>
            </li>
          ))}
        </ul>
      </div>
    );
  }
  
  export default App;