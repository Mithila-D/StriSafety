import React from "react";
import Layout from "../components/Layout/Layout";

const AboutUs = () => {
  return (
    <Layout>
      <div style={styles.container}>
        <div style={styles.overlay}>
          <div style={styles.contentBox}>
            <h1 style={styles.title}>About Us</h1>
            <p style={styles.text}>
              <strong>STRISAFETY</strong> is committed to enhancing women's
              safety by using cutting-edge AI-driven security solutions.
            </p>
            <p style={styles.text}>
              Our system provides real-time surveillance, AI-based distress
              detection, automated alerts, and smart check-ins to ensure a
              secure environment for students in hostels.
            </p>
            <p style={styles.text}>
              By leveraging YOLOv8, OpenCV, DeepFace, and IoT, we create a 24/7
              AI-powered security system that helps students, parents, and
              hostel staff stay connected and secure.
            </p>
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
    backgroundImage: "url('/images/about.png')", // Update with actual image path
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
    background: "rgba(0, 51, 102, 0.6)", // Gradient overlay for better readability
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
  },
  contentBox: {
    background: "rgba(255, 255, 255, 0.2)", // Glass effect
    backdropFilter: "blur(10px)", // Blurry glass effect
    padding: "40px",
    borderRadius: "12px",
    maxWidth: "800px",
    boxShadow: "0 8px 32px rgba(0, 0, 0, 0.2)",
    textAlign: "center",
    border: "1px solid rgba(255, 255, 255, 0.3)",
  },
  title: {
    fontSize: "50px",
    fontWeight: "bold",
    textTransform: "uppercase",
    marginBottom: "20px",
    letterSpacing: "2px",
  },
  text: {
    fontSize: "18px",
    lineHeight: "1.6",
    marginBottom: "15px",
    fontWeight: "500",
    color: "#fff",
  },
};

export default AboutUs;
