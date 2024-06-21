from django.shortcuts import render

# Create your views here.
def result_dtl(request):
    user = {"name": "sourav", "age": 23}
    return render(request, "result/first_result.html", context=user)

def result_for(request):
    students = {"names": ["sourav", "rakib", "ridi", "nisso", "ribbo"], "ages": [23, 23, 23, 23, 23]}
    return render(request, "result/second_result.html", context=students)