# projects/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_detail, name='project_detail'),
]
