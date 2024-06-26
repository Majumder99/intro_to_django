from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import StudentRegistratoinForm
from .models import Student

# Create your views here.
def registerStudent(request):
    if(request.method == 'POST'):
        registerForm = StudentRegistratoinForm(request.POST)
        if(registerForm.is_valid()):
            name = registerForm.cleaned_data['name']
            email = registerForm.cleaned_data['email']
            password = registerForm.cleaned_data['password']
            student = Student(student_name=name, student_email=email, student_password=password)
            student.save()
            
    else:
        registerForm = StudentRegistratoinForm()
    registerForm = StudentRegistratoinForm(auto_id=True)
    return render(request, 'enroll/register.html', {'form': registerForm})