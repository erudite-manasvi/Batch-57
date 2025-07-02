from django.shortcuts import render, HttpResponse

# Create your views here.
def home_view(request):
    return HttpResponse('<h1>Hello World</h1>')

def signup(request):
    return render(request,'Auth_app/index.html')