from django.shortcuts import render
import csv
from .form import *


def upload_files(request):
    form = UploadFileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = UploadFileForm()
        obj = CSVs.objects.get(file_parsed=False)
        with open(obj.file_name.path, 'r') as f:
            patient_records= csv.reader(f)
            for i, record in enumerate(patient_records):
                if i==0:
                    pass
                elif len(record) == 0:
                    pass
                else:
                    mr_number = record[0]
                    first_name = record[1]
                    last_name = record[2]
                    date_of_birth = record[3]
                    visit_date= record[4]
                    reason = record[5]
                    patient = Patients.objects.create(medical_record = mr_number,
                                                    first_name = first_name,last_name= last_name, 
                                                    date_of_birth = date_of_birth)
                    visits = Visit.objects.create(patient=patient, date= visit_date, reason=reason)
        obj.file_parsed = True
        obj.save()
        return render(request, 'record.html')
    return render(request, 'upload.html', {'form': form})

