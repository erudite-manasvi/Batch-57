from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=30,primary_key=True)