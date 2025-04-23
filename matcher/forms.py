from django import forms
from .models import Profile, SportSkill, Game
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateTimeInput


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# In forms.py
class SportSkillForm(forms.ModelForm):
    class Meta:
        model = SportSkill
        fields = ['sport', 'skill_level']  # Use skill_level instead of proficiency
        # Or if you really want to use proficiency in your form, rename the field in your model

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['game_name', 'location', 'time']
        widgets = {
            'time': DateTimeInput(attrs={'type': 'datetime-local'})
        }

from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    SPORT_CHOICES = [
        ('Basketball', 'Basketball'),
        ('Soccer', 'Soccer'),
        ('Tennis', 'Tennis'),
        ('Volleyball', 'Volleyball'),
        ('Swimming', 'Swimming'),
        ('Running', 'Running'),
        ('Cycling', 'Cycling'),
        ('Baseball', 'Baseball'),
        ('Football', 'Football'),
        ('Golf', 'Golf'),
    ]
    
    favorite_sports = forms.MultipleChoiceField(
        choices=SPORT_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'profile_pic', 'favorite_sports', 'skill_level']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us about yourself...'}),
            'location': forms.TextInput(attrs={'placeholder': 'City, State'})
        }
