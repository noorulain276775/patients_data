from django.db import models

# Create your models here.


class Patients(models.Model):
    medical_record = models.IntegerField(unique=True, verbose_name="Medical record number")
    first_name = models.CharField(max_length=256, verbose_name="First name")
    last_name = models.CharField(max_length=256, verbose_name="Last name")
    date_of_birth = models.DateField(verbose_name="Date of birth")

class Visit(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="Date of visit")
    reason = models.TextField(max_length=1000)

