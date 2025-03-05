import JWT from "jsonwebtoken";
import userModel from "../models/userModel.js";
import dotenv from "dotenv";

dotenv.config(); // Load environment variables
//Protected route
export const requireSignIn = async (req, res, next) => {
  try {
    const decode = JWT.verify(req.headers.authorization, process.env.JWT_TOKEN);
    req.user = decode;
    next();
  } catch (error) {
    console.log(error);
  }
};
export const isWarden = async (req, res, next) => {
  try {
    const user = await userModel.findById(req.user._id);

    // Check if the user is a warden (role === 1)
    if (user.role !== 1) {
      return res.status(401).send({
        success: false,
        message: "Unauthorized Access: Only wardens can perform this action",
      });
    }

    next(); // Allow access if the user is a warden
  } catch (error) {
    console.error("Error in Warden Middleware:", error);
    res.status(401).send({
      success: false,
      message: "Error in Warden Middleware",
    });
  }
};
