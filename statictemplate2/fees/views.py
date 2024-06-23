from django.shortcuts import render

# Create your views here.
def show_images(request):
    return render(request, "fee/images.html")