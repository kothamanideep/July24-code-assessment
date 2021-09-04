from django.db import models
class Faculty(models.Model):
    fcode=models.IntegerField()
    name=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    address=models.CharField(max_length=25)
    mobilenumber=models.BigIntegerField()
    username=models.CharField(max_length=40,default='',blank=True)
    password=models.CharField(max_length=40, default='', blank=True)
    
