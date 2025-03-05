import React from "react";

const Footer = () => {
  return (
    <footer style={styles.footer}>
      <div style={styles.container}>
        <h2 style={styles.title}>Stay Connected</h2>
        <p style={styles.text}>
          Follow us on our social platforms for more updates.
        </p>
        <div style={styles.icons}>
          <a
            href="https://www.facebook.com"
            target="_blank"
            rel="noopener noreferrer"
          >
            <i className="fab fa-facebook" style={styles.icon}></i>
          </a>
          <a
            href="https://twitter.com"
            target="_blank"
            rel="noopener noreferrer"
          >
            <i className="fab fa-twitter" style={styles.icon}></i>
          </a>
          <a
            href="https://www.instagram.com"
            target="_blank"
            rel="noopener noreferrer"
          >
            <i className="fab fa-instagram" style={styles.icon}></i>
          </a>
        </div>
        <p style={styles.copy}>© STRISAFETY. All Rights Reserved.</p>
      </div>
    </footer>
  );
};

const styles = {
  footer: {
    backgroundColor: "#003366", // Dark blue
    color: "#ffffff", // White text
    padding: "20px 0",
    textAlign: "center",
  },
  container: {
    maxWidth: "800px",
    margin: "auto",
  },
  title: {
    fontSize: "24px",
    fontWeight: "bold",
  },
  text: {
    fontSize: "16px",
    margin: "10px 0",
  },
  icons: {
    margin: "15px 0",
  },
  icon: {
    fontSize: "24px",
    margin: "0 10px",
    cursor: "pointer",
    color: "#ffffff", // White color for icons
    textDecoration: "none",
  },
  copy: {
    fontSize: "14px",
    marginTop: "10px",
    opacity: "0.8",
  },
};

export default Footer;
