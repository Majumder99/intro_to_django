from django.shortcuts import render

from .forms import StudentRegistratoinForm

# Create your views here.
def showFromData(request):
    registerForm = StudentRegistratoinForm()
    return render(request, 'userregistration.html', {'form': registerForm})