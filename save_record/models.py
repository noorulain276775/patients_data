from django.db import models


class Patients(models.Model):
    medical_record = models.IntegerField(verbose_name="Medical record number")
    first_name = models.CharField(max_length=256, verbose_name="First name")
    last_name = models.CharField(max_length=256, verbose_name="Last name")
    date_of_birth = models.DateField(verbose_name="Date of birth")

    def __str__(self):
        return self.first_name+ ' ' + self.last_name

class Visit(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="Date of visit")
    reason = models.TextField(max_length=1000)

    def __str__(self):
        return self.patient.first_name+ ' ' + self.patient.last_name


class CSVs(models.Model):
    file_name = models.FileField(upload_to='csv')
    file_parsed = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)


