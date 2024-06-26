from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name', 'student_email', 'student_password']
        widgets = {
            'student_password': forms.PasswordInput(),
        }
        labels = {
            'student_name': 'Enter Name',
            'student_email': 'Enter Email',
            'student_password': 'Enter Password',
        }
        error_messages = {
            'student_name': {
                'required': 'Name field is required',
            },
            'student_email': {
                'required': 'Email field is required',
            },
            'student_password': {
                'required': 'Password field is required',
            }
        }
