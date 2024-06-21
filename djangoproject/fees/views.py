from django.shortcuts import render

# Create your views here.
def show_render(request):
    return render(request, 'fees/fees.html')