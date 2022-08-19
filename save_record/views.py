from http.client import HTTPResponse
from django.shortcuts import render
from django.views import View
from .form import *
# from .func import handle_uploaded_file


class RecordsFile(View):

    def get(self, request):
        return render(request, 'record.html')

    # def post(self, request):
    #     form = UploadFileForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         handle_uploaded_file(request.FILES['file'])
    #         return HttpResponseRedirect('/success/url/')
    #     else:
    #         form = UploadFileForm()
    #         return render(request, 'record.html', {'form': form})

class PatientRecords(View):
    def get(self, request):
        return HTTPResponse('Hi you made it')
