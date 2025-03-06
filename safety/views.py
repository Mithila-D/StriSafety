from django.shortcuts import render
from .forms import UploadImageForm
import easyocr
import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from datetime import datetime
from .models import NumberPlateLog  # Import the model for logging number plates

# Predefined number plates and names
plates = ["R177 TC 0530", "MH 12 PQ 2357", "MH 14 AB 4355", "MH 12 MO 5687", "MP 14 CP 2537", "MP 14 KR 3427"]
names = ["Mithila", "Shravani", "Sakshi", "Piyusha", "Janhavi", "Kartiki"]

# Home view
def home(request):
    return render(request, 'safety/home.html')

# Vehicle number plate recognition view
def vehicle_number_plate_recognition(request):
    detected_name = None
    alert_message = None
    uploaded_image = None
    detected_text = None  # Initialize detected_text

    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']

            # Save uploaded image to media folder
            file_path = os.path.join(settings.MEDIA_ROOT, image.name)
            with open(file_path, 'wb') as f:
                for chunk in image.chunks():
                    f.write(chunk)
            saved_path = file_path

            if os.path.exists(saved_path):
                uploaded_image = image.name  # For template display

                # Run OCR
                reader = easyocr.Reader(['en'])
                results = reader.readtext(saved_path)
                detected_text = [text for (_, text, _) in results]

                if detected_text:
                    detected_plate = detected_text[0]  # Assuming first result is the number plate
                    if detected_plate in plates:
                        detected_name = names[plates.index(detected_plate)]
                    else:
                        alert_message = "Oh no, someone else came!!!"

                    # Store result in MySQL using model
                    new_entry = NumberPlateLog(number_plate=detected_plate, owner_name=detected_name)
                    new_entry.save()  # This saves the record in the database

            return render(request, 'safety/number_plate.html', {
                'form': form,
                'uploaded_image': uploaded_image,
                'detected_text': detected_text,
                'detected_name': detected_name,
                'alert_message': alert_message,
                'MEDIA_URL': settings.MEDIA_URL,  # Pass the MEDIA_URL
            })

    else:
        form = UploadImageForm()

    return render(request, 'safety/number_plate.html', {'form': form})



def car_explanation(request):   
    return render(request, 'safety/car2.html')







import google.generativeai as genai
from django.shortcuts import render
from django.conf import settings

# Configure Google Generative AI API
genai.configure(api_key=settings.GENERATIVE_AI_API_KEY)  # You can set this in settings.py

# Function to interact with the chatbot
def chatbot(request):
    chatbot_response = None
    if request.method == 'POST':
        user_input = request.POST.get('user_input')

        if user_input:
            # Select the appropriate model (Gemini)
            model = genai.GenerativeModel("gemini-1.5-pro-latest")

            # Generate a response
            response = model.generate_content(user_input)

            if response and hasattr(response, "text"):
                chatbot_response = response.text + " Thank you dear."  # Customize the response

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

# Get the base directory of the Django project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Construct absolute paths for the model and vectorizer
model_path = os.path.join(BASE_DIR, 'safety', 'ml_models', 'logistic_regression_model.pkl')
vectorizer_path = os.path.join(BASE_DIR, 'safety', 'ml_models', 'tfidf_vectorizer.pkl')

# Load the model and vectorizer
try:
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
except FileNotFoundError as e:
    print(f"Error: {e}")
    model, vectorizer = None, None

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Preprocessing function
def clean_text(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#\w+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    text = ' '.join(word for word in text.split() if word not in stop_words)
    return text

# Sentiment Prediction Function
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

# View to handle feedback submission
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

            return redirect('feedback_list')  # Redirect to feedback display page

    else:
        form = FeedbackForm()

    return render(request, "safety/feedback_form.html", {"form": form})


# View to display all feedback
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
        "media_url": settings.MEDIA_URL,  # ✅ Pass MEDIA_URL to the template
    })
