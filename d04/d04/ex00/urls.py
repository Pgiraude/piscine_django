from django.shortcuts import render

def index(request):
    return render(request, 'ex00/index.html')
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]