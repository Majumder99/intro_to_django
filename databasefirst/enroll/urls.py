from django.urls import path
from . import views

urlpatterns = [
    path("userdata/", views.show_data)
]
