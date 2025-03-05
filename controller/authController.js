// export const registerController = async (req, res) => {};
import userModel from "../models/userModel.js";
import { hashPassword, comaprePassword } from "../helpers/authHelper.js";
import JWT from "jsonwebtoken";
export const registerController = async (req, res) => {
  try {
    // Fetching the data
    const {
      name,
      email,
      password,
      phone,
      parentContact,
      guardianContact,
      emergencyContact,
      hostelID,
      roomNumber,
      address,
    } = req.body;

    // Validation of data
    if (!name) return res.status(400).send({ message: "Name is required" });
    if (!email) return res.status(400).send({ message: "Email is required" });
    if (!password)
      return res.status(400).send({ message: "Password is required" });
    if (!phone) return res.status(400).send({ message: "Phone is required" });
    if (!parentContact)
      return res.status(400).send({ message: "Parent contact is required" });
    if (!guardianContact)
      return res.status(400).send({ message: "Guardian contact is required" });
    if (!emergencyContact)
      return res.status(400).send({ message: "Emergency contact is required" });
    if (!hostelID)
      return res.status(400).send({ message: "Hostel ID is required" });
    if (!roomNumber)
      return res.status(400).send({ message: "Room number is required" });
    if (!address)
      return res.status(400).send({ message: "Address is required" });

    // Checking for existing user
    const existingUser = await userModel.findOne({ email });
    if (existingUser) {
      return res.status(200).send({
        success: false,
        message: "Already registered, please login.",
      });
    }

    // Hashing the password before saving
    const hashedPassword = await hashPassword(password);

    // Creating a new user
    const user = new userModel({
      name,
      email,
      password: hashedPassword,
      phone,
      parentContact,
      guardianContact,
      emergencyContact,
      hostelID,
      roomNumber,
      address,
    });

    // Save user to database
    await user.save();

    // Sending success response
    res.status(201).send({
      success: true,
      message: "User registered successfully",
      user,
    });
  } catch (error) {
    console.error("Error in registering user:", error);
    res.status(500).send({
      success: false,
      message: "Error in registration",
      error: error.message,
    });
  }
};

export const loginController = async (req, res) => {
  try {
    const { email, password } = req.body;

    // Validation
    if (!email || !password) {
      return res.status(400).send({
        success: false,
        message: "Invalid email or password",
      });
    }

    // Check if user exists
    const user = await userModel.findOne({ email });
    if (!user) {
      return res.status(404).send({
        success: false,
        message: "Email is not registered",
      });
    }

    // Compare password
    const match = await comaprePassword(password, user.password);
    if (!match) {
      return res.status(401).send({
        success: false,
        message: "Invalid Password",
      });
    }

    // Generate token
    const token = JWT.sign({ _id: user._id }, process.env.JWT_TOKEN, {
      expiresIn: "7d",
    });

    // Send response
    res.status(200).send({
      success: true,
      message: "Login successful",
      user: {
        _id: user._id,
        name: user.name,
        email: user.email,
        phone: user.phone,
        parentContact: user.parentContact,
        guardianContact: user.guardianContact,
        emergencyContact: user.emergencyContact,
        hostelID: user.hostelID,
        roomNumber: user.roomNumber,
        address: user.address,
        role: user.role, // Role 0 = student, 1 = admin/warden
      },
      token,
    });
  } catch (error) {
    console.error("Error in login:", error);
    res.status(500).send({
      success: false,
      message: "Error in login",
      error: error.message,
    });
  }
};

export const testController = (req, res) => {
  console.log("Protected Routes");
};
