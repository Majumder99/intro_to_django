from django.urls import path
from . import views
urlpatterns = [
    path('learndj/', views.fees_view),
    path('learnpj/', views.fees_edit)
]
