from .views import *
from django.urls import path

urlpatterns = [
    path('record/', RecordsFile.as_view()),
    path('patients/', PatientRecords.as_view())  
]
