from rest_framework import serializers
from doctors.models import Doctor

class doctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields=('doctorcode','name','address','speciality','username','password')