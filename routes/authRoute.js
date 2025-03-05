import express from "express";
import {
  loginController,
  registerController,
  testController,
} from "../controller/authController.js";
import { requireSignIn, isWarden } from "../middleware/authMiddleware.js";
//router object
const router = express.Router();

//routing
router.post("/register", registerController);
router.post("/login", loginController);
router.get("/test", requireSignIn, isWarden, testController);
export default router;
