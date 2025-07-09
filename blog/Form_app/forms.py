from django import forms
from .models import FormUpload

# class FileUploadForm(forms.Form):
#     name=forms.CharField(label='File Name',max_length=100)
#     file=forms.FileField(label='Select File')

class FileUploadForm(forms.ModelForm):
    class Meta:
        model=FormUpload
        fields='__all__'