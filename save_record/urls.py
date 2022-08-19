from .views import *
from django.urls import path

urlpatterns = [
    path('record/', upload_files),  
]
