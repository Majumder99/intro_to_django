from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def learn_django(request):
    return HttpResponse("This is the learn_django view")

def edit_django(request):
    return HttpResponse("This is the learn_django edit")

def index(request):
    return HttpResponse("This is the index view")