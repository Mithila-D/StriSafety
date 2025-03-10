from django.db import models

# Create your models here.

from django.db import models
from django.db import models

class NumberPlateLog(models.Model):  
    number_plate = models.CharField(max_length=255)  
    owner_name = models.CharField(max_length=255, null=True, blank=True)  
    timestamp = models.DateTimeField(auto_now_add=True)  

    class Meta:  
        db_table = "safety_numberplatelog"   

    def __str__(self):  
        return self.number_plate  





from django.db import models

class User(models.Model):
    UserName = models.CharField(max_length=255, unique=True)
    Password = models.CharField(max_length=255) 

    def __str__(self):
        return self.UserName









from django.db import models

class Feedback(models.Model):
    user_name = models.CharField(max_length=255)
    feedback = models.TextField()
    sentiment = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.sentiment}"






from django.db import models

class WardenDetail(models.Model):
    warden_name = models.CharField(max_length=255)
    time = models.TimeField()
    date = models.DateField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.warden_name
