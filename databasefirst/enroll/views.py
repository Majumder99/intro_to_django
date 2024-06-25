from django.shortcuts import render
from enroll.models import Student

# Create your views here.
def show_data(request):
    students = Student.objects.all()
    print('data from database', students)
    return render(request, 'showdata.html', context={'stus': students})