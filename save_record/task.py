from .models import *
from celery import shared_task
import pandas as pd


@shared_task()
def saving_csv_in_database(arr):

    # Unique records
    df = pd.DataFrame(arr)
    removed_duplicate_Records= df.drop_duplicates(subset=['mr_number', 'date', 'reason'])
    unique_records = removed_duplicate_Records.to_dict('records')

    patient_instances = []
    for record in unique_records:
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
    success = print("Yay! Unique data has been saved to database successfully!")
    return success
