import cv2
import torch
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")  # Use "yolov8n.pt" for fastest inference

# Initialize webcam
cap = cv2.VideoCapture(0)  # 0 for default webcam

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection
    results = model(frame, stream=True)

    # Draw bounding boxes
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0].item()
            cls = int(box.cls[0].item())
            label = f"{model.names[cls]}: {conf:.2f}"

            # Draw rectangle and label
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Show output
    cv2.imshow("Fast YOLOv8 Object Detection", frame)

    # **Exit Conditions**
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit on 'q' key press
        break
    if cv2.getWindowProperty("Fast YOLOv8 Object Detection", cv2.WND_PROP_VISIBLE) < 1:  # Exit if window is closed
        break

cap.release()
cv2.destroyAllWindows()
