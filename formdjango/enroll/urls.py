from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.showFromData),
    path("success/", views.thankyou),
    path("error/", views.errorpage)
]
