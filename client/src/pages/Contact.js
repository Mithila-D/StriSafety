// import React from "react";
// import Layout from "../components/Layout/Layout";
// const Contact = () => {
//   return (
//     <Layout>
//       <h1>Contact Us Page</h1>
//     </Layout>
//   );
// };

// export default Contact;
import React from "react";
import Layout from "../components/Layout/Layout";

const Contact = () => {
  return (
    <Layout>
      <div style={styles.container}>
        <div style={styles.overlay}>
          <div style={styles.formBox}>
            <h1 style={styles.title}>Contact Us</h1>
            <p style={styles.text}>
              We’d love to hear from you! Fill out the form below.
            </p>

            <form style={styles.form}>
              <input
                type="text"
                placeholder="Your Name"
                style={styles.input}
                required
              />
              <input
                type="email"
                placeholder="Your Email"
                style={styles.input}
                required
              />
              <textarea
                placeholder="Your Message"
                rows="4"
                style={styles.textarea}
                required
              ></textarea>
              <button type="submit" style={styles.button}>
                Send Message
              </button>
            </form>
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
    backgroundImage: "url('/images/contact.png')", // Update with actual image path
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
    background: "rgba(0, 51, 102, 0.6)", // Faint blue overlay
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
  },
  formBox: {
    background: "rgba(255, 255, 255, 0.2)", // Glass effect
    backdropFilter: "blur(10px)", // Blurry glass effect
    padding: "40px",
    borderRadius: "12px",
    maxWidth: "500px",
    boxShadow: "0 8px 32px rgba(0, 0, 0, 0.2)",
    textAlign: "center",
    border: "1px solid rgba(255, 255, 255, 0.3)",
  },
  title: {
    fontSize: "40px",
    fontWeight: "bold",
    marginBottom: "10px",
    letterSpacing: "1px",
  },
  text: {
    fontSize: "18px",
    marginBottom: "20px",
  },
  form: {
    display: "flex",
    flexDirection: "column",
    gap: "15px",
  },
  input: {
    width: "100%",
    padding: "12px",
    borderRadius: "5px",
    border: "none",
    outline: "none",
    fontSize: "16px",
    backgroundColor: "rgba(255, 255, 255, 0.7)", // Light transparent input field
  },
  textarea: {
    width: "100%",
    padding: "12px",
    borderRadius: "5px",
    border: "none",
    outline: "none",
    fontSize: "16px",
    backgroundColor: "rgba(255, 255, 255, 0.7)",
  },
  button: {
    padding: "12px",
    fontSize: "18px",
    fontWeight: "bold",
    color: "#003366", // Dark blue text
    backgroundColor: "#ffcc00", // Yellow button
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
    transition: "0.3s",
  },
};

export default Contact;
