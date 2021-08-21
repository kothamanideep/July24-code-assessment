from django.db import models

# Create your models here.
class Patient(models.Model):
    patientcode=models.BigIntegerField()
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    disease=models.CharField(max_length=100)
    admitstatus=models.CharField(max_length=100)
    
    