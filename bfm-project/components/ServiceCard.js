// pages/index.js
import React from 'react';
import ServiceCard from '../components/ServiceCard';

const Home = () => {
  return (
    <div>
      <h1>Welcome to Budget Friendly Movers</h1>
      {/* You can use the ServiceCard component here */}
      <ServiceCard title="Local Moving" description="Description for local moving service." />
    </div>
  );
};

export default Home;

