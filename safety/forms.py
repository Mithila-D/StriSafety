from django import forms

class UploadImageForm(forms.Form):
    image = forms.ImageField()






from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['user_name', 'feedback']
