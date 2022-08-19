from django import forms
from .models import *

class RecordForm(forms.ModelForm):

   class Meta:
      model = Patients
      fields = ['medical_record','first_name','last_name', 'date_of_birth']

class UploadFileForm(forms.Form):
    file = forms.FileField()