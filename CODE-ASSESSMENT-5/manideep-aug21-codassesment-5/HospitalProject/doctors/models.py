from django.db import models

# Create your models here.
class Doctor(models.Model):
    doctorcode=models.BigIntegerField()
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    speciality=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.BigIntegerField()
    
    