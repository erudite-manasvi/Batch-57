from django.shortcuts import render
from .forms import FileUploadForm
from .models import FormUpload
from django.http import JsonResponse

# Create your views here.
def file_upload_form(req):
    if req.method=='GET':
        form = FileUploadForm()
        return render(req,'Form_app/index.html',{'form':form})
    
    if req.method=='POST':
        form = FileUploadForm(req.POST,req.FILES)

        if form.is_valid():
            form.save()

            return JsonResponse({
                'success':True
            },status=200)
        
        return JsonResponse({
            "success":False,
            "error":form.errors
        },status=500)
