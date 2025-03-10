from django.contrib import admin
from django.urls import path, include
from . import views
from .views import car_entry, chatbot, feedback_list, pop_top_warden, recognition_graph_view, stop_face_detection, student_dash, submit_feedback, team, vehicle_number_plate_recognition, face_detect_page, face_detect_stream, warden_allocate, warden_dash, warden_dets
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('number-plate/', vehicle_number_plate_recognition, name='number_plate_recognition'),
    path('chatbot/', chatbot, name='chatbot'),
    path('feedback/', submit_feedback, name='submit_feedback'),
    path('feedback-list/', feedback_list, name='feedback_list'),
    path('car-entry/', car_entry, name='car_entry'),
    path('car2/', views.car_explanation, name='car_explanation'), 
    
     path('face-detect/', face_detect_page, name='face_detect_page'),
    path('face-detect/stream/', face_detect_stream, name='face_detect_stream'),
    path('face-detect/stop/', stop_face_detection, name='stop_face_detection'),
    
    path('face_recognize/', views.face_recognize_page, name='face_recognize_page'),
    path('face_recognize/stream/', views.face_recognize_stream, name='face_recognize_stream'),
    path('face_recognize/stop/', views.stop_webcam_view, name='stop_webcam'),
    
    path('warden/recognition-graph/', recognition_graph_view, name='recognition_graph'),
    
    path('warden/allocate/', warden_allocate, name='warden_allocate'),
    path('warden/details/', warden_dets, name='warden_dets'),
    path("warden/pop_top/", pop_top_warden, name="pop_top_warden"),
    
    path("warden/dash/", warden_dash, name="warden_dash"),
    path("student_dash/", student_dash, name="student_dash"),
    
    path("team/", team, name="team"),
    
    path('signin/', views.login_view, name='signin'),  
    path('signup/', views.signup_view, name='signup'),
    
]
 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
