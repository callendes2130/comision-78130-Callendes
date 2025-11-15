"""
from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    avatar = forms.ImageField(required=False)
    class Meta:
        model = User  
        fields = ("username", "email", "password1", "password2", 'avatar')
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Profile.objects.get_or_create(user=user, avatar=self.cleaned_data.get('avatar'))
        return user

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User  
        fields = ("username", "email", "first_name", "last_name")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile  
        fields = ("pais", "fecha_de_nacimiento", "direccion", 'avatar')
        widgets = {"fecha_de_nacimiento": forms.DateInput(attrs={"type": "date"})}
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("pais", "fecha_de_nacimiento", "direccion", "avatar")
        widgets = {"fecha_de_nacimiento": forms.DateInput(attrs={"type": "date"})}