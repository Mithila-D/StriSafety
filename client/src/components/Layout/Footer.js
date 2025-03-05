// import React from "react";
// import { Link } from "react-router-dom";
// const Footer = () => {
//   return (
//     <footer style={styles.footer}>
//       <div style={styles.container}>
//         <h2 style={styles.title}>Stay Connected</h2>
//         <p style={styles.text}>
//           Follow us on our social platforms for more updates.
//         </p>
//         <div>
//           <Link to="/home">Home</Link>
//           <Link to="/aboutus">About Us</Link>
//           <Link to="/contact">Contact</Link>
//         </div>
//         <div style={styles.icons}>
//           <a
//             href="https://www.facebook.com"
//             target="_blank"
//             rel="noopener noreferrer"
//           >
//             <i className="fab fa-facebook" style={styles.icon}></i>
//           </a>
//           <a
//             href="https://twitter.com"
//             target="_blank"
//             rel="noopener noreferrer"
//           >
//             <i className="fab fa-twitter" style={styles.icon}></i>
//           </a>
//           <a
//             href="https://www.instagram.com"
//             target="_blank"
//             rel="noopener noreferrer"
//           >
//             <i className="fab fa-instagram" style={styles.icon}></i>
//           </a>
//         </div>
//         <p style={styles.copy}>© STRISAFETY. All Rights Reserved.</p>
//       </div>
//     </footer>
//   );
// };

// const styles = {
//   footer: {
//     backgroundColor: "#003366", // SAME Dark Blue as Header
//     color: "#ffffff", // White text
//     padding: "20px 0",
//     textAlign: "center",
//     boxShadow: "0px -4px 10px rgba(0, 0, 0, 0.1)", // Slight shadow at the top
//   },
//   container: {
//     maxWidth: "800px",
//     margin: "auto",
//   },
//   title: {
//     fontSize: "24px",
//     fontWeight: "bold",
//   },
//   text: {
//     fontSize: "16px",
//     margin: "10px 0",
//   },
//   icons: {
//     margin: "15px 0",
//   },
//   icon: {
//     fontSize: "24px",
//     margin: "0 10px",
//     cursor: "pointer",
//     color: "#ffffff", // White color for icons
//     textDecoration: "none",
//     transition: "0.3s", // Smooth hover effect
//   },
//   copy: {
//     fontSize: "14px",
//     marginTop: "10px",
//     opacity: "0.8",
//   },
// };

// export default Footer;
import React from "react";
import { Link } from "react-router-dom";

const Footer = () => {
  return (
    <footer style={styles.footer}>
      <div style={styles.container}>
        <h2 style={styles.title}>Stay Connected</h2>
        <p style={styles.text}>
          Follow us on our social platforms for more updates.
        </p>

        {/* Navigation Links */}
        <div style={styles.navLinks}>
          <Link to="/home" style={styles.navLink}>
            Home
          </Link>
          <Link to="/aboutus" style={styles.navLink}>
            About Us
          </Link>
          <Link to="/contact" style={styles.navLink}>
            Contact
          </Link>
        </div>

        {/* Social Media Icons */}
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
    backgroundColor: "#003366", // SAME Dark Blue as Header
    color: "#ffffff", // White text
    padding: "20px 0",
    textAlign: "center",
    boxShadow: "0px -4px 10px rgba(0, 0, 0, 0.1)", // Slight shadow at the top
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
  navLinks: {
    display: "flex",
    justifyContent: "center",
    gap: "20px",
    margin: "15px 0",
  },
  navLink: {
    textDecoration: "none",
    color: "#ffffff", // White text
    fontSize: "16px",
    fontWeight: "500",
    padding: "5px 10px",
    transition: "0.3s",
  },
  navLinkHover: {
    color: "#ffcc00", // Yellow on hover
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
    transition: "0.3s",
  },
  copy: {
    fontSize: "14px",
    marginTop: "10px",
    opacity: "0.8",
  },
};

export default Footer;
