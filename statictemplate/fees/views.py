from django.shortcuts import render

# Create your views here.
def show_images(request):
    return render(request, "fees/images.html")