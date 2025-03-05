// import React from "react";

// const Header = () => {
//   return (
//     <div>
//       <h1>Header</h1>
//     </div>
//   );
// };

// export default Header;
import React, { useState } from "react";

const Header = () => {
  const [activeTab, setActiveTab] = useState("Home");

  return (
    <nav style={styles.navbar}>
      <div style={styles.logo}>STRISAFETY</div>
      <ul style={styles.navLinks}>
        {["Home", "About Us", "Contact"].map((item) => (
          <li key={item}>
            <a
              href="#"
              style={{
                ...styles.navLink,
                ...(activeTab === item ? styles.activeNavLink : {}),
              }}
              onClick={() => setActiveTab(item)}
            >
              {item}
            </a>
          </li>
        ))}
      </ul>
      <div style={styles.authButtons}>
        <a href="#" style={styles.registerButton}>
          Register
        </a>
        <a href="#" style={styles.loginButton}>
          Login
        </a>
      </div>
    </nav>
  );
};

const styles = {
  navbar: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    padding: "15px 30px",
    backgroundColor: "#003366", // Dark Blue
    color: "#ffffff", // White text
    boxShadow: "0px 4px 10px rgba(0, 0, 0, 0.1)",
  },
  logo: {
    fontSize: "22px",
    fontWeight: "bold",
  },
  navLinks: {
    listStyle: "none",
    display: "flex",
    gap: "20px",
    margin: 0,
    padding: 0,
  },
  navLink: {
    textDecoration: "none",
    color: "#ffffff",
    fontSize: "16px",
    fontWeight: "500",
    transition: "0.3s",
    padding: "5px 10px",
  },
  activeNavLink: {
    backgroundColor: "#ffcc00", // Yellow background for active link
    color: "#003366", // Dark blue text
    borderRadius: "5px",
    padding: "5px 15px",
  },
  authButtons: {
    display: "flex",
    gap: "10px",
  },
  registerButton: {
    backgroundColor: "#ffcc00", // Yellow
    color: "#003366",
    padding: "8px 15px",
    borderRadius: "5px",
    textDecoration: "none",
    fontWeight: "bold",
    transition: "0.3s",
  },
  loginButton: {
    backgroundColor: "transparent",
    color: "#ffffff",
    padding: "8px 15px",
    borderRadius: "5px",
    border: "2px solid #ffcc00",
    textDecoration: "none",
    fontWeight: "bold",
    transition: "0.3s",
  },
};

export default Header;
