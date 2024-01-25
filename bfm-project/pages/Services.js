// pages/Services.js
import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import ServiceCard from '../components/ServiceCard';

const Services = () => {
  return (
    <div>
      <Header />
      <main>
        <h1>Our Services</h1>
        <ServiceCard title="Local Moving" description="Description for local moving service." />
        <ServiceCard title="Long Distance Moving" description="Description for long-distance moving service." />
        {/* Add more service cards as needed */}
      </main>
      <Footer />
    </div>
  );
};

export default Services;
