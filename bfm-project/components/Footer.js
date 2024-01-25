// components/Footer.js
import Link from 'next/link';
import styles from '../styles/Footer.module.css';

const Footer = () => (
  <footer className={styles.footer}>
    <div className={styles.footerContent}>
      <div className={styles.footerSection}>
        <h3>Quick Links</h3>
        <ul>
          <li>
            <Link href="/">Home</Link>
          </li>
          <li>
            <Link href="/about">About Us</Link>
          </li>
          <li>
            <Link href="/services">Services</Link>
          </li>
          <li>
            <Link href="/contact">Contact</Link>
          </li>
        </ul>
      </div>
      <div className={styles.footerSection}>
        <h3>Contact Us</h3>
        <p>Address: Your Address</p>
        <p>Email: your@email.com</p>
        <p>Phone: +123 456 789</p>
      </div>
    </div>
    <div className={styles.footerBottom}>
      <p>&copy; 2024 Budget Friendly Movers. All rights reserved.</p>
    </div>
  </footer>
);

export default Footer;
