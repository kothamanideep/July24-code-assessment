
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from doctors.serializers import doctorSerializer
from doctors.models import Doctor
from rest_framework.parsers import JSONParser
from rest_framework import status 
# Create your views here.

def register(request):
    return render(request,"register.html")

def login(request):
    return render(request,"login.html")


@csrf_exempt
def doctor(request):
    if(request.method=="POST"):
        mydic=JSONParser().parse(request)
        doctor_serialize=doctorSerializer(data=mydic)
        if (doctor_serialize.is_valid()):
            doctor_serialize.save()
            return JsonResponse(doctor_serialize.data)
        else:
            return HttpResponse("error in serilazation")

    else:
        return HttpResponse("sucess")


@csrf_exempt
def doctorlist(request):
    if(request.method=="GET"):
        doctors=Doctor.objects.all()
        doctor_serializer=doctorSerializer(doctors,many=True)
        return JsonResponse(doctor_serializer.data,safe=False)

@csrf_exempt
def mydoctors(request,fetchid):
    try:
        doctor1=Doctor.objects.get(id=fetchid)
        if(request.method=="GET"):
            doctor_serializer=doctorSerializer(doctor1)
            return JsonResponse(doctor_serializer.data,safe=False)

        if(request.method=="DELETE"):
            doctor1.delete()
            return HttpResponse("Deleted")

        if(request.method=="PUT"):
            mydic=JSONParser().parse(request)
            doctor_serialize=doctorSerializer(doctor1,data=mydic)
            if (doctor_serialize.is_valid()):
                doctor_serialize.save()
                return JsonResponse(doctor_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(doctor_serialize.errors)
    except Doctor.DoesNotExist:
        return HttpResponse("invalid syntax",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def mydoctor1(request,fetchcode):
    try:
        doctor1=Doctor.objects.get(doctorcode=fetchcode)
        if(request.method=="GET"):
            doctor_serializer=doctorSerializer(doctor1)
            return JsonResponse(doctor_serializer.data,safe=False)

    except Doctor.DoesNotExist:
        return HttpResponse("invalid syntax")