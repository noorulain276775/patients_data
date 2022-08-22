from django.shortcuts import render
import pandas as pd
from .models import Visit, Patients
from .task import saving_csv_in_database
from .form import *

def upload_files(request):
    form = UploadFileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        csvfile = request.FILES['file_name']
        try:
            data = pd.read_csv(csvfile)
            dropping_missing_values= data.dropna()
        except FileNotFoundError:
            return render(request, 'error.html')
        arr = dropping_missing_values.to_dict('records')

        # Duplicate records
        duplicate_records = dropping_missing_values[dropping_missing_values.duplicated()]
        array_of_duplicate_records = duplicate_records.to_dict('records')

        context = {'d': arr, 'a': array_of_duplicate_records}
        saving_csv_in_database.delay(arr)
        return render(request, 'upload.html', context)
    return render(request, 'record.html', {'form': form})


def view_all_records(request):
    patient_record = Visit.objects.all().order_by('-date')
    return render(request, 'all_records.html', {'all_data': patient_record})