from django.shortcuts import render, HttpResponse
from .models import Person
from django.http import JsonResponse

from .serializers import PersonSerializer

# Create your views here.
def home_view(request):
    return HttpResponse('<h1>Hello World</h1>')

def signup(request):
    return render(request,'Auth_app/index.html')

def get_data(request):
    if request.method=='GET':
        data=Person.objects.all()
        serialized_data = PersonSerializer(data,many=True)
        return JsonResponse(serialized_data.data,safe=False)