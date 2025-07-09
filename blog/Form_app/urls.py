
from django.urls import path
from .views import file_upload_form
urlpatterns = [
    path('file/',file_upload_form)
]