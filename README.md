# AI-Powered Girls' Hostel Security  

An advanced security system designed to enhance safety in girls' hostels by leveraging AI-powered surveillance, visitor management, emergency alerts, and real-time monitoring. This system integrates facial recognition, number plate recognition, object detection, and sentiment analysis to create a smarter, safer, and more efficient hostel environment.  

---

## Features  

### AI-Powered Security & Monitoring  
- Face Recognition – Identifies authorized individuals using DeepFace.Recognized names are saved in WomenSafetyWebsite\WomenSafetyWebsite\person_recog.json
- Object Detection – Detects and stores in file called WomenSafetyWebsite\WomenSafetyWebsite\Detected_Obj.json suspicious objects using YOLOv8.  
- Vehicle Number Plate Recognition – Tracks vehicle number-plates using YOLOv8 and EasyOCR and then check if they are registered or not. If not gives alert. Also stores seen nuberplate and data in 127.0.0.1:8000/car-entry/  
- Unauthorized Person Alerts – Sends real-time alerts for unknown individuals.  
- The graph for late check-in or check-out is seen with a threshold line of 9pm.

### Hostel Management & Student Safety  
- Check-In/Check-Out Tracking – Logs students' entry and exit times.   
- Emergency Warden Contact – Displays real-time details of on-duty wardens.  
- Feedback System with Sentiment Analysis – Analyzes student feedback for safety concerns.  

### AI Chatbot & Communication  
- AI Chatbot for Hostel Queries – Answers security-related questions.  
- Mental Health Support Chatbot – Provides emotional support to students.  
- Real-Time Alerts & Notifications – Sends SMS alerts to parents and wardens using Twilio.  
- Warden-Student Chat System – Enables direct communication in case of emergencies.  

---

## Tech Stack  

| Technology | Purpose |
|--------------|------------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Django |
| Database | MySQL |
| AI/ML | YOLOv8, OpenCV, DeepFace, EasyOCR |

---

## Project Structure  

```
StriSafety/
│── WomenSafetyWebsite/
│   ├── known_faces/
│   ├── media/   
│   ├── safety/               # app
│   │   ├── templates/safety/                
│   │   ├── manage.py
│   ├── WomenSafetyWebsite/
│   ├── Detected_Obj.json
│   ├── person_recog.json
│   ├── requirements.txt             
│── README.md                 
```

---

## Installation & Setup  

### 1. Clone the Repository  

git clone https://github.com/Mithila-D/StriSafety.git



### 2. Create and Activate a Virtual Environment  

python -m venv venv

venv\Scripts\activate  # Windows

source venv/bin/activate  # macOS/Linux


### 3. Install Dependencies  

pip install -r requirements.txt
 

### 4. Run the Django Server  
 
cd WomenSafetyWebsite

python manage.py runserver
 
Now, open **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** in your browser.

---

## Usage Guide  

- **Home Page:** The main landing page, located in the **safety** app.
  
- **Student Dashboard:**

--Chatbot

--warden details

--Feedback fill

--Check feedbacks

- **Warden Dashboard:**
  
--Fill Warden Details
  
--number plate Recognition

--face recognition

--Obj detection

--see feedbacks

--check time of people entry



---




