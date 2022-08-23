# patient-record
## Celery and Redis with Django

### Used celery with django and sendgrid to schedule a task and send email notification
- Notifying user via email about duplicate data already exist in database and saving only unique data.

### View records
- User can view all the data from the database.

### Submit the csv file
- User uploads csv file and then the csv files appears that also highlights the duplicate data within the csv file with a screen alert for user.


# Tools

- Django (function-based views (backend), django forms)
- Django templates (HTML, CSS, Javascript (Frontend))
- Celery with redis (for scheduling task)
- Pandas (for csv file analysis, like removing empty values and dealing with duplicates)

