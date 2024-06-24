from django.shortcuts import render

# Create your views here.
def fees_view(request):
    return render(request, 'feesview.html')

def about_us(request):
    return render(request, 'aboutus.html')

def contact_us(request):
    return render(request, 'contactus.html')