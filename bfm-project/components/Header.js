// components/Header.js
import Link from 'next/link';
import styles from '../styles/Header.module.css';

const Header = () => (
  <header className={styles.header}>
    <div className={styles.logo}>
      <Link href="/">
        {/* Use a div or another non-interactive element instead of <a> here */}
        <div>
          <img src="/images/logo.jpeg" alt="BFM Logo" />
        </div>
      </Link>
    </div>
    <nav className={styles.nav}>
      <Link href="/">Home</Link>
      <Link href="/about">About Us</Link>
      <Link href="/services">Services</Link>
      <Link href="/contact">Contact</Link>
      <Link href="/quote"></Link>
      <Link href="/quote">
        <div className={styles.quoteLink}>Get a Quote</div>
      </Link>


      
    </nav>
  </header>
);

export default Header;

