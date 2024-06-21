from django.urls import path
from . import views

urlpatterns = [
    path('django-learn/', views.show_render, name='fees'),
]
