from django.contrib import admin
from django.urls import path, include
from . import views
from .views import car_entry, chatbot, feedback_list, submit_feedback, vehicle_number_plate_recognition
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('number-plate/', vehicle_number_plate_recognition, name='number_plate_recognition'),
    path('chatbot/', chatbot, name='chatbot'),
    path('feedback/', submit_feedback, name='submit_feedback'),
    path('feedback-list/', feedback_list, name='feedback_list'),
    path('car-entry/', car_entry, name='car_entry'),
]

# Serve static files correctly
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serve media files correctly
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
