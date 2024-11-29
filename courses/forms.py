from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Course, Enrollment

# User Signup Form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Enrollment Form
class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['course']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter courses to show only those that the user is not already enrolled in
        self.fields['course'].queryset = Course.objects.exclude(enrollments__student=user)

