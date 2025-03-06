import easyocr
import cv2
import matplotlib.pyplot as plt
import os

# Set the correct image path (Make sure the image exists in the project directory)
image_path = "safety/static/sample_data/b.jpg"  # Update path as per your setup

# Check if the file exists
if not os.path.exists(image_path):
    print(f"Error: File not found at {image_path}")
else:
    print("✅ Image found! Proceeding...")

    # Load EasyOCR model
    reader = easyocr.Reader(['en'])

    # Read and display the image
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert for display

    # Run OCR
    results = reader.readtext(image)

    # Display image
    plt.imshow(image_rgb)
    plt.axis("off")
    plt.show()

    # Print detected text
    for (bbox, text, prob) in results:
        print(f"Detected Text: {text} (Confidence: {prob:.2f})")
