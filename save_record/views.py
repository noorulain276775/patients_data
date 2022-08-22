from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
import pandas as pd
from .models import Patients, Visit
from .form import *


def upload_files(request):
    form = UploadFileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        csvfile = request.FILES['file_name']
        try:
            data = pd.read_csv(csvfile.name)
        except FileNotFoundError:
            return render(request, 'error.html')
        arr = data.to_dict('records')
        context = {'d': arr}
        patient_instances = []
        for record in arr:
            patient_instance = Visit(
                patient=Patients.objects.create(
                    medical_record=record['mr_number'],
                    first_name=record['first_name'],
                    last_name=record['last_name'],
                    date_of_birth=record['dob']
                ),
                date=record['date'],
                reason=record['reason']
            )
            patient_instances.append(patient_instance)
        Visit.objects.bulk_create(patient_instances)
        return render(request, 'upload.html', context)
    return render(request, 'record.html', {'form': form})

def view_all_records(request):
    patient_record = Visit.objects.all().order_by('-date')
    return render(request, 'all_records.html', {'all_data': patient_record})






