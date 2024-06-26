from django.shortcuts import render
from .forms import StudentRegistrationForm
from .models import Student

# Create your views here.
def registerStudent(request):
    if(request.method == 'POST'):
        registerForm = StudentRegistrationForm(request.POST)
        if(registerForm.is_valid()):
            name = registerForm.cleaned_data['student_name']
            email = registerForm.cleaned_data['student_email']
            password = registerForm.cleaned_data['student_password']
            student = Student(student_name=name, student_email=email, student_password=password)
            student.save()
            
    else:
        registerForm = StudentRegistrationForm()
    registerForm = StudentRegistrationForm(auto_id=True)
    return render(request, 'enroll/register.html', {'form': registerForm})