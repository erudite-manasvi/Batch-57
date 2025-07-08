from django.shortcuts import render, HttpResponse
from .models import Person
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .serializers import PersonSerializer

# Create your views here.
def home_view(request):
    return HttpResponse('<h1>Hello World</h1>')

def signup(request):
    return render(request,'Auth_app/index.html')

@csrf_exempt
def get_data(request):
    if request.method=='GET':
        data=Person.objects.all()
        serialized_data = PersonSerializer(data,many=True)
        return JsonResponse(serialized_data.data,safe=False)
    
    if request.method == 'POST':
        input_data = request.body # raw JSON(bytes)
        raw_data = json.loads(input_data) # raw JSON(bytes) -> Python dict
        sd = PersonSerializer(data=raw_data) #desrialization

        if sd.is_valid():
            sd.save()
            return JsonResponse({
                "success":True,
                "message":"Data saved successfully"
            }, status=201)
        
        return JsonResponse({
            "success":False,
            "message":sd.errors
        })
    
@csrf_exempt
def get_data_by_id(request,email):
    
    data = Person.objects.get(email=email) #finding data from DB

    if request.method=='GET':
        sd = PersonSerializer(data) #serialization
        return JsonResponse(sd.data,safe=False)
    
    if request.method == 'PUT':
        input_data=json.loads(request.body)

        sd = PersonSerializer(data,data=input_data)

        if sd.is_valid():
            sd.save()

            return JsonResponse({
                "success":True,
                "message":"Data updated successfully"
            },status=200)
        
        return JsonResponse({
            "success":False,
            "message":sd.errors
        },status=500)
    
    if request.method == 'PATCH':
        input_data=json.loads(request.body)

        sd = PersonSerializer(data,data=input_data,partial=True)

        if sd.is_valid():
            sd.save()

            return JsonResponse({
                "success":True,
                "message":"Data updated successfully"
            },status=200)
        
        return JsonResponse({
            "success":False,
            "message":sd.errors
        },status=500)
    
    if request.method == 'DELETE':
        data.delete()

        return JsonResponse({
            "success":True,
            "message":"Data deleted successfully"
        },status=200)