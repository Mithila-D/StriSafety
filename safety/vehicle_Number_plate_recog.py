import easyocr
import cv2
import matplotlib.pyplot as plt
import os
 
image_path = "safety/static/sample_data/b.jpg"   
 
if not os.path.exists(image_path):
    print(f"Error: File not found at {image_path}")
else:
    print("Image found! ")
 
    reader = easyocr.Reader(['en'])
 
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)   
 
    results = reader.readtext(image)
 
    plt.imshow(image_rgb)
    plt.axis("off")
    plt.show()
 
    for (bbox, text, prob) in results:
        print(f"Detected Text: {text} (Confidence: {prob:.2f})")
