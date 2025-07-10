from django.shortcuts import render
from .models import User
from django.http import JsonResponse

# Create your views here.
def login(request):

    if request.session.get('username'): #home
        return JsonResponse({
            'message':"Already LoggedIn",
            "user":request.session.get('username')
        })

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        try:
            user = User.objects.get(username=username)

            if user.password==password:
                request.session['username']=username
                request.session.set_expiry(15)

                return JsonResponse({
                    "success":True,
                    "message":"User LoggedIn Successfully"
                },status=200)
            
        except Exception as e:
            return JsonResponse({
                    "success":True,
                    "message":str(e)
                },status=500)
        
    return render(request,'Session_app/login.html')