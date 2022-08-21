from .views import *
from django.urls import path

urlpatterns = [
    path('record/', upload_files),  
    path('all_records/', view_all_records),  
]
