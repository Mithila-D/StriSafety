import mongoose from "mongoose";

const userSchema = new mongoose.Schema(
  {
    name: {
      type: String,
      required: true,
      trim: true,
    },
    email: {
      type: String,
      required: true,
      unique: true,
      lowercase: true,
      trim: true,
    },
    password: {
      type: String,
      required: true,
      minlength: 6,
    },
    phone: {
      type: String,
      required: true,
      trim: true,
    },
    parentContact: {
      type: String,
      required: true,
      trim: true, // Direct parent's phone number
    },
    guardianContact: {
      type: String,
      required: true,
      trim: true, // Another guardian/emergency contact
    },
    emergencyContact: {
      type: String,
      required: true,
      trim: true, // Secondary emergency contact
    },
    hostelID: {
      type: String,
      required: true,
      unique: true,
    },
    roomNumber: {
      type: String,
      required: true,
    },
    address: {
      type: Object,
      required: true,
    },
    checkInTime: {
      type: Date,
      default: null,
    },
    checkOutTime: {
      type: Date,
      default: null,
    },
    status: {
      type: String,
      enum: ["inside", "outside"],
      default: "inside",
    },
    wearableDeviceID: {
      type: String,
      default: null,
    },
    role: {
      type: Number,
      default: 0,
    },
  },
  { timestamps: true }
);

export default mongoose.model("User", userSchema);
