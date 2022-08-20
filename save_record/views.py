from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
import pandas as pd
from .models import Patients, Visit
from .form import *


def upload_files(request):
    form = UploadFileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        csvfile = request.FILES['file_name']
        data = pd.read_csv(csvfile.name)
        arr = data.to_dict('records')
        context = {'d': arr}
        for record in arr:
            visit_instances = [Visit(
                patient=Patients.objects.create(
                    medical_record=record['mr_number'],
                    first_name=record['first_name'],
                    last_name=record['last_name'],
                    date_of_birth=record['dob']
                ),
                date=record['date'],
                reason=record['reason']
            )]
        Visit.objects.bulk_create(visit_instances)
        return render(request, 'upload.html', context)
    return render(request, 'record.html', {'form': form})


# def upload_files(request):
#     form = UploadFileForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         csvfile = request.FILES['file_name']
#         data = pd.read_csv(csvfile.name)
#         form.save()
#         form = UploadFileForm()
#         obj = CSVs.objects.get(file_parsed=False)
#         with open(obj.file_name.path, 'r') as f:
#             patient_records= csv.reader(f)
#             for i, record in enumerate(patient_records):
#                 if i==0:
#                     pass
#                 elif len(record) == 0:
#                     pass
#                 else:
#                     mr_number = record[0]
#                     first_name = record[1]
#                     last_name = record[2]
#                     date_of_birth = record[3]
#                     visit_date= record[4]
#                     reason = record[5]
#                     patient = Patients.objects.create(medical_record = mr_number,
#                                                     first_name = first_name,last_name= last_name,
#                                                     date_of_birth = date_of_birth)
#                     visits = Visit.objects.create(patient=patient, date= visit_date, reason=reason)
#         obj.file_parsed = True
#         obj.save()
#         return render(request, 'upload.html')
#     return render(request, 'record.html', {'form': form})
