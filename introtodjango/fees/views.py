from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def fees_view(request):
    return HttpResponse('fees view')

def fees_edit(request):
    return HttpResponse('fees edit')