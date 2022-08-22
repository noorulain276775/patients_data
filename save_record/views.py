from django.shortcuts import render
import pandas as pd
from .models import Visit
from .task import saving_csv_in_database
from .form import *

def upload_files(request):
    try:
        form = UploadFileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            csvfile = request.FILES['file_name']
            try:
                # Dropping the missing values
                data = pd.read_csv(csvfile, dtype={'mr_number': 'Int32'}).dropna()
            except FileNotFoundError:
                return render(request, 'error.html')

            # convert dataframes into dictionary

            arr = data.to_dict('records')

            # Duplicate records in csv
            duplicate_records = data[data.duplicated()]
            array_of_duplicate_records = duplicate_records.to_dict('records')

            # Sending data to frontend

            context = {'d': arr, 'a': array_of_duplicate_records}

            # Used Celery for running a task in the background (task.py)
            saving_csv_in_database.delay(arr)

            # IF we have duplicate records in csv then render this template
            if len(array_of_duplicate_records)> 0:
                return render(request, 'record_duplicate.html', context)

            # Otherwise this
            else:
                return render(request, 'upload.html', context)
        return render(request, 'record.html', {'form': form})
    except:
        return render(request, 'error.html')


def view_all_records(request):
    try:
        # We got the records in ascending order order_by('date') if it was descending then ('-date')
        patient_record = Visit.objects.all().order_by('date')
        return render(request, 'all_records.html', {'all_data': patient_record})
    except:
        return render(request, 'error.html')
