from django.http import StreamingHttpResponse
from django.shortcuts import render
from .forms import UploadImageForm
import easyocr
import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from datetime import datetime
from .models import NumberPlateLog  
 
plates = ["R177 TC 0530", "MH 12 PQ 2357", "MH 14 AB 4355", "MH 12 MO 5687", "MP 14 CP 2537", "MP 14 KR 3427"]
names = ["Mithila", "Shravani", "Sakshi", "Piyusha", "Janhavi", "Kartiki"]
 
def home(request):
    return render(request, 'safety/home.html')
 
def vehicle_number_plate_recognition(request):
    detected_name = None
    alert_message = None
    uploaded_image = None
    detected_text = None   

    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
 
            file_path = os.path.join(settings.MEDIA_ROOT, image.name)
            with open(file_path, 'wb') as f:
                for chunk in image.chunks():
                    f.write(chunk)
            saved_path = file_path

            if os.path.exists(saved_path):
                uploaded_image = image.name   
 
                reader = easyocr.Reader(['en'])
                results = reader.readtext(saved_path)
                detected_text = [text for (_, text, _) in results]

                if detected_text:
                    detected_plate = detected_text[0] 
                    if detected_plate in plates:
                        detected_name = names[plates.index(detected_plate)]
                    else:
                        alert_message = "Oh no, someone else came!!!"
 
                    new_entry = NumberPlateLog(number_plate=detected_plate, owner_name=detected_name)
                    new_entry.save()  

            return render(request, 'safety/number_plate.html', {
                'form': form,
                'uploaded_image': uploaded_image,
                'detected_text': detected_text,
                'detected_name': detected_name,
                'alert_message': alert_message,
                'MEDIA_URL': settings.MEDIA_URL,  
            })

    else:
        form = UploadImageForm()

    return render(request, 'safety/number_plate.html', {'form': form})



def car_explanation(request):   
    return render(request, 'safety/car2.html')







import google.generativeai as genai
from django.shortcuts import render
from django.conf import settings
 
genai.configure(api_key=settings.GENERATIVE_AI_API_KEY)   
 
def chatbot(request):
    chatbot_response = None
    if request.method == 'POST':
        user_input = request.POST.get('user_input')

        if user_input:
 
            model = genai.GenerativeModel("gemini-1.5-pro-latest")
 
            response = model.generate_content(user_input)

            if response and hasattr(response, "text"):
                chatbot_response = response.text + " Thank you dear."  

    return render(request, 'safety/chatbot.html', {'chatbot_response': chatbot_response})















import os
import joblib
import re
import nltk
from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback
from nltk.corpus import stopwords
from django.db import connection
 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
 
model_path = os.path.join(BASE_DIR, 'safety', 'ml_models', 'logistic_regression_model.pkl')
vectorizer_path = os.path.join(BASE_DIR, 'safety', 'ml_models', 'tfidf_vectorizer.pkl')
 
try:
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
except FileNotFoundError as e:
    print(f"Error: {e}")
    model, vectorizer = None, None

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
 
def clean_text(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#\w+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    text = ' '.join(word for word in text.split() if word not in stop_words)
    return text
 
def predict_sentiment(text):
    if model is None or vectorizer is None:
        return "Model not loaded properly"

    cleaned_text = clean_text(text)
    X_text = vectorizer.transform([cleaned_text])
    prediction = model.predict(X_text)[0]

    if prediction == 1:
        return "Positive Sentiment"
    elif prediction == -1:
        return "Hate Speech"
    else:
        return "Neutral/Non-Hate Speech"
 
def submit_feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback_text = form.cleaned_data['feedback']
            sentiment = predict_sentiment(feedback_text)

            # Save to database
            feedback_instance = form.save(commit=False)
            feedback_instance.sentiment = sentiment
            feedback_instance.save()

            return redirect('feedback_list')   

    else:
        form = FeedbackForm()

    return render(request, "safety/feedback_form.html", {"form": form})









# import os
# import joblib
# import re
# import nltk
# from django.shortcuts import render, redirect
# from .forms import FeedbackForm
# from .models import Feedback
# from nltk.corpus import stopwords
# from django.db import connection
 
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
 
# model_path = os.path.join(BASE_DIR, 'safety', 'ml_models', 'logistic_regression_model.pkl')
# vectorizer_path = os.path.join(BASE_DIR, 'safety', 'ml_models', 'tfidf_vectorizer.pkl')
 
# try:
#     model = joblib.load(model_path)
#     vectorizer = joblib.load(vectorizer_path)
# except FileNotFoundError as e:
#     print(f"Error: {e}")
#     model, vectorizer = None, None

# nltk.download('stopwords')
# stop_words = set(stopwords.words('english'))
 
# def clean_text(text):
#     text = re.sub(r'http\S+', '', text)
#     text = re.sub(r'@\w+', '', text)
#     text = re.sub(r'#\w+', '', text)
#     text = re.sub(r'[^\w\s]', '', text)
#     text = text.lower()
#     text = ' '.join(word for word in text.split() if word not in stop_words)
#     return text
 
# def predict_sentiment(text):
#     if model is None or vectorizer is None:
#         return "Model not loaded properly"

#     cleaned_text = clean_text(text)
#     X_text = vectorizer.transform([cleaned_text])
#     prediction = model.predict(X_text)[0]

#     if prediction == 1:
#         return "Positive Sentiment"
#     elif prediction == -1:
#         return "Bad review"
#     else:
#         return "Neutral"
 
# def submit_feedback(request):
#     if request.method == "POST":
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             feedback_text = form.cleaned_data['feedback']
#             sentiment = predict_sentiment(feedback_text)
 
#             feedback_instance = form.save(commit=False)
#             feedback_instance.sentiment = sentiment
#             feedback_instance.save()

#             return redirect('feedback_list')   

#     else:
#         form = FeedbackForm()

#     return render(request, "safety/feedback_form.html", {"form": form})


# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def submit_feedback(request):
#     if request.method == "POST":
#         feedback_text = request.POST.get("feedback_text")

#         if feedback_text:
          
#             return JsonResponse({"message": "Feedback submitted successfully"})

#         return JsonResponse({"error": "Feedback text is required"}, status=400)

#     return JsonResponse({"error": "Invalid request"}, status=400)





 
def feedback_list(request):
    feedbacks = Feedback.objects.all().order_by('-timestamp')
    return render(request, "safety/feedback_list.html", {"feedbacks": feedbacks})


from django.shortcuts import render
from .models import NumberPlateLog
from django.shortcuts import render
from django.db import connection

from django.shortcuts import render
from django.db import connection

from django.conf import settings

def car_entry(request):
    query = "SELECT id, number_plate, owner_name, timestamp FROM safety_numberplatelog ORDER BY timestamp DESC;"
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
 
    logs = [
        {
            "id": row[0],
            "number_plate": row[1],
            "owner_name": row[2] if row[2] is not None else "",   
            "timestamp": row[3]
        }
        for row in rows
    ]

    return render(request, "safety/car_entry.html", {
        "logs": logs,
        "media_url": settings.MEDIA_URL,   
    })








from django.shortcuts import render
from .forms import UploadImageForm
import easyocr
import os
import json
from datetime import datetime
from django.conf import settings
from django.db import connection
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import cv2
import torch
from ultralytics import YOLO
 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DETECTED_OBJ_PATH = os.path.join(BASE_DIR, "Detected_Obj.json")
 
model = YOLO("yolov8n.pt")
 
plates = ["R177 TC 0530", "MH 12 PQ 2357", "MH 14 AB 4355", "MH 12 MO 5687", "MP 14 CP 2537", "MP 14 KR 3427"]
names = ["Mithila", "Shravani", "Sakshi", "Piyusha", "Janhavi", "Kartiki"]

def home(request):
    return render(request, 'safety/home.html')

def vehicle_number_plate_recognition(request):
    detected_name = None
    alert_message = None
    uploaded_image = None
    detected_text = None   

    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']

            file_path = os.path.join(settings.MEDIA_ROOT, image.name)
            with open(file_path, 'wb') as f:
                for chunk in image.chunks():
                    f.write(chunk)
            saved_path = file_path

            if os.path.exists(saved_path):
                uploaded_image = image.name

                reader = easyocr.Reader(['en'])
                results = reader.readtext(saved_path)
                detected_text = [text for (_, text, _) in results]

                if detected_text:
                    detected_plate = detected_text[0]  
                    if detected_plate in plates:
                        detected_name = names[plates.index(detected_plate)]
                    else:
                        alert_message = "Oh no, someone else came!!!"
 
                    store_detected_object(detected_plate, 1.0)

            return render(request, 'safety/number_plate.html', {
                'form': form,
                'uploaded_image': uploaded_image,
                'detected_text': detected_text,
                'detected_name': detected_name,
                'alert_message': alert_message,
                'MEDIA_URL': settings.MEDIA_URL,  
            })

    else:
        form = UploadImageForm()

    return render(request, 'safety/number_plate.html', {'form': form})




def car_explanation(request):   
    return render(request, 'safety/car2.html')





import google.generativeai as genai

genai.configure(api_key=settings.GENERATIVE_AI_API_KEY)   

def chatbot(request):
    chatbot_response = None
    if request.method == 'POST':
        user_input = request.POST.get('user_input')

        if user_input:
            model = genai.GenerativeModel("gemini-1.5-pro-latest")
            response = model.generate_content(user_input)

            if response and hasattr(response, "text"):
                chatbot_response = response.text + " Thank you dear."

    return render(request, 'safety/chatbot.html', {'chatbot_response': chatbot_response})



def car_entry(request):
    query = "SELECT id, number_plate, owner_name, timestamp FROM safety_numberplatelog ORDER BY timestamp DESC;"
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

    logs = [
        {
            "id": row[0],
            "number_plate": row[1],
            "owner_name": row[2] if row[2] is not None else "",   
            "timestamp": row[3]
        }
        for row in rows
    ]

    return render(request, "safety/car_entry.html", {
        "logs": logs,
        "media_url": settings.MEDIA_URL,   
    })
















# #################################################
# def generate_frames():
#     cap = cv2.VideoCapture(0)    
#     while cap.isOpened():
#         success, frame = cap.read()
#         if not success:
#             break

#         results = model(frame, stream=True)

#         for result in results:
#             for box in result.boxes:
#                 x1, y1, x2, y2 = map(int, box.xyxy[0])
#                 conf = box.conf[0].item()
#                 cls = int(box.cls[0].item())
#                 label = f"{model.names[cls]}: {conf:.2f}"

#                 cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
#                 cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
 
#                 store_detected_object(model.names[cls], conf)

#         _, buffer = cv2.imencode('.jpg', frame)
#         frame_bytes = buffer.tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

#     cap.release()

# def face_detect_stream(request):
#     return StreamingHttpResponse(generate_frames(), content_type="multipart/x-mixed-replace; boundary=frame")

# def face_detect_page(request):
#     return render(request, 'safety/Face_Detect.html')
 
# def store_detected_object(obj_name, probability):
#     detected_data = {
#         "id": int(datetime.now().timestamp()),   
#         "object_detected": obj_name,
#         "probability": round(probability, 2),
#         "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     }
 
#     if os.path.exists(DETECTED_OBJ_PATH):
#         with open(DETECTED_OBJ_PATH, "r") as file:
#             try:
#                 data = json.load(file)
#             except json.JSONDecodeError:
#                 data = []
#     else:
#         data = []
 
#     data.append(detected_data)
 
#     with open(DETECTED_OBJ_PATH, "w") as file:
#         json.dump(data, file, indent=4)

#     print(f"Stored: {detected_data}")


from django.http import StreamingHttpResponse, JsonResponse
import cv2
import os
import json
from datetime import datetime
from django.shortcuts import render
 
stop_webcam = False

DETECTED_OBJ_PATH = "Detected_Obj.json"   

def generate_frames():
    global stop_webcam
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        if stop_webcam:
            break  

        success, frame = cap.read()
        if not success:
            break

        results = model(frame, stream=True)

        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = box.conf[0].item()
                cls = int(box.cls[0].item())
                label = f"{model.names[cls]}: {conf:.2f}"

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                store_detected_object(model.names[cls], conf)

        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    cap.release()

def face_detect_stream(request):
    global stop_webcam
    stop_webcam = False   
    return StreamingHttpResponse(generate_frames(), content_type="multipart/x-mixed-replace; boundary=frame")

def face_detect_page(request):
    return render(request, 'safety/Face_Detect.html')

def stop_face_detection(request):
    
    global stop_webcam
    stop_webcam = True
    return JsonResponse({"status": "stopped"})

def store_detected_object(obj_name, probability):
    detected_data = {
        "id": int(datetime.now().timestamp()),
        "object_detected": obj_name,
        "probability": round(probability, 2),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    if os.path.exists(DETECTED_OBJ_PATH):
        with open(DETECTED_OBJ_PATH, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(detected_data)

    with open(DETECTED_OBJ_PATH, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Stored: {detected_data}")



###################################




import os
import json
import cv2
import uuid
from datetime import datetime, timedelta
from django.http import StreamingHttpResponse, JsonResponse
from django.shortcuts import render
from deepface import DeepFace
 
PERSON_RECOG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "person_recog.json")
KNOWN_FACES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "known_faces")
 
stop_webcam = False  
 
def load_existing_data():
    if os.path.exists(PERSON_RECOG_PATH):
        try:
            with open(PERSON_RECOG_PATH, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

def store_recognized_person(person_name):
    existing_data = load_existing_data()
    existing_entries = {(entry["person_name"], entry["timestamp"]) for entry in existing_data}

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     
    if (person_name, timestamp) not in existing_entries:
        recognized_data = {
            "id": int(str(uuid.uuid4().int)[:10]),  # Generate unique 10-digit ID
            "person_name": person_name,
            "timestamp": timestamp
        }

        existing_data.append(recognized_data)

        with open(PERSON_RECOG_PATH, "w") as file:
            json.dump(existing_data, file, indent=4)

        print(f"Recognized and stored: {recognized_data}")
def recognize_faces():
    global stop_webcam
    cap = cv2.VideoCapture(0)

    try:
        while cap.isOpened():
            if stop_webcam:  
                break 

            success, frame = cap.read()
            if not success:
                break

            try:
           
                result = DeepFace.find(
                    img_path=frame,
                    db_path=KNOWN_FACES_DIR,
                    enforce_detection=False
                )

                if len(result) > 0:
                    person_name = os.path.basename(result[0]['identity'][0]).split('.')[0]
                    store_recognized_person(person_name)
 
                    cv2.putText(frame, person_name, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            except Exception as e:
                print("Recognition error:", e)

            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    finally:
        cap.release()  
        cv2.destroyAllWindows()   


def face_recognize_stream(request):
    global stop_webcam
    stop_webcam = False  
    return StreamingHttpResponse(recognize_faces(), content_type="multipart/x-mixed-replace; boundary=frame")

def face_recognize_page(request):
    return render(request, 'safety/Face_Recognize.html')

def stop_webcam_view(request):
    global stop_webcam
    stop_webcam = True   
    return JsonResponse({"status": "stopped"})





import os
import json
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from io import BytesIO

PERSON_RECOG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "person_recog.json")

def plot_recognition_graph():
    if not os.path.exists(PERSON_RECOG_PATH):
        return None

    with open(PERSON_RECOG_PATH, "r") as file:
        data = json.load(file)

    if not data:
        return None   

    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])  
    df['date'] = df['timestamp'].dt.date
    df['hour'] = df['timestamp'].dt.hour
 
    start_date = datetime(2025, 3, 1).date()
    end_date = datetime(2025, 3, 15).date()
    df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

    # 6 AM to 12 AM
    time_slots = list(range(6, 24 + 1))  

    plt.figure(figsize=(12, 6))
 
    for person in df['person_name'].unique():
        person_data = df[df['person_name'] == person]
        plt.scatter(person_data['date'], person_data['hour'], label=person)
 
    plt.axhline(y=21, color='red', linestyle='dotted', linewidth=2.5, label="9 PM Threshold")
 
    plt.xticks(pd.date_range(start=start_date, end=end_date, freq='D'), 
               [d.strftime("%d") for d in pd.date_range(start=start_date, end=end_date, freq='D')], 
               fontsize=10)
 
    plt.yticks(time_slots, [f"{hour}:00" for hour in time_slots], fontsize=10)
 
    plt.xlabel("Date (March)", fontsize=12)
    plt.ylabel("Hours", fontsize=12)
    plt.title(" Student Check in timimngs(March 1-15)", fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
 
    buffer = BytesIO()
    plt.savefig(buffer, format="png", bbox_inches="tight")
    buffer.seek(0)
    return buffer

def recognition_graph_view(request):
    graph = plot_recognition_graph()
    if graph:
        return HttpResponse(graph.getvalue(), content_type="image/png")
    return HttpResponse("No data available", content_type="text/plain")
























from django.shortcuts import render, redirect
from .models import WardenDetail

def warden_allocate(request):
    if request.method == "POST":
        warden_name = request.POST.get("warden_name")
        time = request.POST.get("time")
        date = request.POST.get("date")
        contact_number = request.POST.get("contact_number")

        if warden_name and time and date and contact_number:
            WardenDetail.objects.create(
                warden_name=warden_name,
                time=time,
                date=date,
                contact_number=contact_number
            )
            return redirect("warden_allocate")

    wardens = WardenDetail.objects.all()
    return render(request, "safety/warden_allocate.html", {"wardens": wardens})


def pop_top_warden(request):
    
    if request.method == "POST":
        first_warden = WardenDetail.objects.order_by("id").first()
        if first_warden:
            first_warden.delete()
    return redirect("warden_allocate")


def warden_dets(request):
    wardens = WardenDetail.objects.all()
    return render(request, 'safety/warden_dets.html', {'wardens': wardens})


from django.shortcuts import render

def warden_dash(request):
    return render(request, "safety/Warden_dash.html")


def student_dash(request):
    return render(request, "safety/Student_dash.html")



def team(request):
    return render(request, "safety/Team.html")















from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User 
from django.contrib.auth.hashers import make_password, check_password
from django.db import IntegrityError

def signup_view(request):
    if request.method == 'POST':
        UserName = request.POST.get('UserName')
        Password = request.POST.get('Password')
        if User.objects.filter(UserName=UserName).exists():
            messages.error(request, 'Username already taken. Please choose a different one.')
            return redirect('signup')  
        try:
            hashed_password = make_password(Password)
            user = User(UserName=UserName, Password=hashed_password)
            user.save()
            messages.success(request, 'User registered successfully. You can now log in.')
            return redirect('signin')  
        except IntegrityError:
            messages.error(request, 'An error occurred during registration. Please try again.')
            return redirect('signup') 
    return render(request, 'safety/SignUp.html') 

def login_view(request):
    if request.method == 'POST':
        UserName = request.POST.get('UserName')
        Password = request.POST.get('Password')
        try:
            user = User.objects.get(UserName=UserName)
            if check_password(Password, user.Password):
                return redirect('warden_dash')  
            else:
                messages.error(request, 'Incorrect password. Please try again.')
                return redirect('signin')
        except User.DoesNotExist:
            messages.error(request, 'User not found or incorrect credentials.')
            return redirect('signin')
    return render(request, 'safety/SignIn.html')  



