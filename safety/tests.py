from django.test import TestCase

# Create your tests here.
from django.db import models

class NumberPlateLog(models.Model):
    number_plate = models.CharField(max_length=20)
    name = models.CharField(max_length=50, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False 

    def __str__(self):
        return f"{self.number_plate} - {self.name} ({self.timestamp})"
