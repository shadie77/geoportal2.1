from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Enter your firstname')
    last_name = forms.CharField(max_length=30, required=True, help_text='Enter your surname')
    email = forms.EmailField(max_length=254, required=True, help_text="Required. Insert a valid email address")
    class Meta:
        model= User
        fields = ["first_name", 'last_name', 'username','email','password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name'}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields= ["phone_number"]