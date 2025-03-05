import React from "react";
import Layout from "../components/Layout/Layout";
import { Link } from "react-router-dom";

const PageNotFound = () => {
  return (
    <Layout>
      <div style={styles.container}>
        <h1 style={styles.title}>404</h1>
        <p style={styles.text}>
          Oops! The page you're looking for doesn't exist.
        </p>
        <Link to="/home" style={styles.homeButton}>
          Go Back Home
        </Link>
      </div>
    </Layout>
  );
};

const styles = {
  container: {
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
    height: "100vh",
    backgroundColor: "rgba(0, 51, 102, 0.2)", // Faint Blue with 20% opacity
    color: "#003366", // Dark blue text for contrast
    textAlign: "center",
    padding: "20px",
  },
  title: {
    fontSize: "80px",
    fontWeight: "bold",
    margin: "10px 0",
  },
  text: {
    fontSize: "20px",
    marginBottom: "20px",
  },
  homeButton: {
    textDecoration: "none",
    backgroundColor: "#ffcc00", // Yellow Button
    color: "#003366", // Dark Blue Text
    padding: "10px 20px",
    borderRadius: "5px",
    fontSize: "18px",
    fontWeight: "bold",
    transition: "0.3s",
  },
};

export default PageNotFound;
