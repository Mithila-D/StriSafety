import express from "express";
import dotenv from "dotenv";
import morgan from "morgan";
import connectDB from "./config/db.js";
//rest object
const app = express();

//confugire env
dotenv.config();

//middleware
app.use(express.json());
app.use(morgan("dev"));

//database config
connectDB();

//rest api
app.get("/", (req, res) => {
  res.send("<h1>Welcome to SHE</h1>");
});

//PORT
const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log(`Server Running on ${process.env.DEV_MODE} mode on port ${PORT}`);
});
