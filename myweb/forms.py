from django import forms
from .models import *

class Contactform(forms.ModelForm):
    class Meta:
        model=contactmodel
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '👤 Your Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder': '📧 Your Email Address'}),
            'message': forms.Textarea(attrs={'placeholder': '💬 Type your message here...'}),
        }