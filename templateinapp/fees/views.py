from django.shortcuts import render

# Create your views here.
def inside(request):
    return render(request, 'fees/first.html')