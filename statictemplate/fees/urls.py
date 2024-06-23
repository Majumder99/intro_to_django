from django.urls import path
from . import views

urlpatterns = [
    path("images", views.show_images, name="show_images")
]
