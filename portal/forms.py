from django import forms
from .models import Complaint
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['title', 'description', 'department', 'priority', 'attachment']

class StatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['status']
