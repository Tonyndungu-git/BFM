// pages/index.js
import React, { useState, useEffect } from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';

const Home = () => {
  const [movers, setMovers] = useState([]);

  useEffect(() => {
    // Fetch movers data from the API
    if (movers.length === 0) {
      fetch('/api/movers')
        .then((response) => response.json())
        .then((data) => setMovers(data))
        .catch((error) => console.error('Error fetching movers data:', error));
    }
  }, [movers]); // Only run the effect when movers array changes

  return (
    <div>
      <Header />
      <main>
        <h1>Welcome to Budget Friendly Movers</h1>

        {/* Display movers data */}
        <h2>Our Movers:</h2>
        <ul>
          {movers.map((mover) => (
            <li key={mover.id}>{mover.name} - {mover.location}</li>
          ))}
        </ul>
      </main>
      <Footer />
    </div>
  );
};

export default Home;
