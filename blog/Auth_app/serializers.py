from rest_framework import serializers
from .models import Person

# class PersonSerializer(serializers.Serializer):
#     name=serializers.CharField()
#     phone=serializers.CharField()
#     email=serializers.EmailField()

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'