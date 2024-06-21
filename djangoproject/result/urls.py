from django.urls import path
from . import views

urlpatterns = [
    path('result-dtl/', views.result_dtl, name='fees'),
    path('result-for/', views.result_for, name='fees'),
]
