import React from "react";
import { Link } from "react-router-dom";
import Layout from "../components/Layout/Layout";

const HomePage = () => {
  return (
    <Layout>
      <div style={styles.container}>
        <div style={styles.overlay}>
          <div style={styles.content}>
            <h1 style={styles.highlightedText}>
              Committed to Enhancing{" "}
              <span style={styles.wordHighlight}>Women's Safety</span>
            </h1>
            <p style={styles.text}>
              Our mission is to create a secure and empowering environment for
              women through AI-driven surveillance, real-time monitoring, and
              emergency alerts. Safety is not just a priority—it's a necessity.
            </p>
            <p style={styles.text}>
              Together, we can build a world where every woman feels safe,
              protected, and valued.
            </p>

            {/* Register & Login Buttons */}
            <div style={styles.buttonContainer}>
              <Link to="/register" style={styles.registerButton}>
                Register
              </Link>
              <Link to="/login" style={styles.loginButton}>
                Login
              </Link>
            </div>

            {/* Chatbot Button */}
            <div style={styles.chatbotContainer}>
              <button style={styles.chatbotButton}>
                Chat with AI Assistant 🤖
              </button>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
};

const styles = {
  container: {
    position: "relative",
    height: "100vh",
    backgroundImage: "url('/images/home.png')", // Update with actual image path
    backgroundSize: "cover",
    backgroundPosition: "center",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    textAlign: "center",
    color: "#ffffff",
  },
  overlay: {
    position: "absolute",
    top: 0,
    left: 0,
    width: "100%",
    height: "100%",
    background: "rgba(0, 51, 102, 0.6)", // Dark blue transparent overlay
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
  },
  content: {
    background: "rgba(255, 255, 255, 0.2)", // Glass effect
    backdropFilter: "blur(10px)",
    padding: "40px",
    borderRadius: "12px",
    maxWidth: "800px",
    boxShadow: "0 8px 32px rgba(0, 0, 0, 0.2)",
    textAlign: "center",
    border: "1px solid rgba(255, 255, 255, 0.3)",
  },
  highlightedText: {
    fontSize: "50px",
    fontWeight: "bold",
    marginBottom: "20px",
    letterSpacing: "1.5px",
    color: "#ffcc00", // Yellow color for main text
    textShadow: "2px 2px 10px rgba(255, 204, 0, 0.7)", // Glowing effect
    animation: "glow 2s infinite alternate", // Animated glow effect
  },
  wordHighlight: {
    color: "#ff6600", // Bright orange for "Women's Safety"
    textShadow: "2px 2px 10px rgba(255, 102, 0, 0.7)", // Soft glowing effect
  },
  text: {
    fontSize: "18px",
    lineHeight: "1.6",
    marginBottom: "15px",
    fontWeight: "500",
  },
  buttonContainer: {
    display: "flex",
    justifyContent: "center",
    gap: "15px",
    marginTop: "20px",
  },
  registerButton: {
    textDecoration: "none",
    backgroundColor: "#ffcc00", // Yellow Button
    color: "#003366",
    padding: "12px 20px",
    borderRadius: "5px",
    fontSize: "18px",
    fontWeight: "bold",
    transition: "0.3s",
  },
  loginButton: {
    textDecoration: "none",
    backgroundColor: "#ffffff", // White Button
    color: "#003366",
    padding: "12px 20px",
    borderRadius: "5px",
    fontSize: "18px",
    fontWeight: "bold",
    transition: "0.3s",
  },
  chatbotContainer: {
    marginTop: "30px",
  },
  chatbotButton: {
    backgroundColor: "#ffffff",
    color: "#003366",
    padding: "12px 25px",
    fontSize: "18px",
    fontWeight: "bold",
    borderRadius: "30px",
    cursor: "pointer",
    border: "none",
    transition: "0.3s",
  },
};

export default HomePage;
