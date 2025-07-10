from django.contrib.auth.signals import user_logged_in #signal
from django.contrib.auth.models import User #model - sender

def login_success(request, **kwargs): # receiver function
    print('I am receiver fuction!!')
    print(request)
    print(kwargs['user'].email)


user_logged_in.connect(login_success,sender=User)