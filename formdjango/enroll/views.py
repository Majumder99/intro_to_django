from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import StudentRegistratoinForm

# Create your views here.
def showFromData(request):
    #  'password', 're_password', 'class_attr', 'date_type'
    # initial={'name': 'Your Name', 'email': 'Your Email'},
    if(request.method == 'POST'):
        registerForm = StudentRegistratoinForm(request.POST)
        if(registerForm.is_valid()):
            name = registerForm.cleaned_data['name']
            email = registerForm.cleaned_data['email']
            # password = registerForm.cleaned_data['password']
            # re_password = registerForm.cleaned_data['re_password']
            # class_attr = registerForm.cleaned_data['class_attr']
            # date_type = registerForm.cleaned_data['date_type']
            # print(name, email, password, re_password, class_attr, date_type)
            print(name, email)
            # return render(request, 'success.html', {'name': name})
            return HttpResponseRedirect('/enroll/success/')
            
    else:
        registerForm = StudentRegistratoinForm()
        # return render(request, 'error.html', {'form': registerForm}) 
    registerForm = StudentRegistratoinForm(auto_id=True, field_order=['email', 'name',])
    return render(request, 'userregistration.html', {'form': registerForm})
    
    
def thankyou(request):
    return render(request, 'success.html')
def errorpage(request):
    return render(request, 'error.html')