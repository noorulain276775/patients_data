"""
Using celery and sendgrid for email notification and adding only unique data in database

"""

from .models import *
from celery import shared_task
import pandas as pd
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from datetime import datetime


@shared_task()
def saving_csv_in_database(arr):

    try:
        # Got Unique records from a function (upload_files) in django views
        df = pd.DataFrame(arr)
        removed_duplicate_Records = df.drop_duplicates(
            subset=['mr_number', 'date', 'reason'])
        unique_records = removed_duplicate_Records.to_dict('records')

        # trying to save entries in database, filtering out duplicate records

        patient_instances = []
        duplicate_records_in_database = []
        for record in unique_records:

            # As date in datebase has datetime format while date in record['date'] is in string therefore converting the
            # string date into datetime format so that we can do matching in order to check if the similar records already exist

            date = datetime.strptime(record['date'], '%Y-%m-%d %H:%M:%S')

            # Django query for check duplication with respect to mr_number, date and reason
            
            duplicate= Visit.objects.filter(patient__medical_record=record['mr_number'], date=date, reason=record['reason'])
            if len(duplicate)>0:
                duplicate_records_in_database.append(record)
            else:
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

        # Email notification only if you have duplicate records 

        if len(duplicate_records_in_database)>0:
            print("There are 24 duplicated records")
            print('sending the mail to notify user')
            message = Mail(
                from_email='noorulainibrahim75@gmail.com',
                to_emails='noorulainibrahim123456@gmail.com',
                subject='Duplicate Records',
                html_content='<strong>You have some duplicate records</strong>')
            try:
                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print("error")

        # Create unique entries in database 
        # We are printing the results to check if everyting is working fine in celery task

        if len(patient_instances)> 0:
            print(f'total number of {len(patient_instances)} new records are being added in database')
            Visit.objects.bulk_create(patient_instances)
            success = print("Yay! Unique data has been saved to database successfully!")
            return success
        else:
            print("No new records")
            no_new_data = print("No new data to save")
            return no_new_data
    except:
        error= print("Something went wrong")
        return error