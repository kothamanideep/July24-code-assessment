
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from patients.serializers import patientSerializer
from patients.models import Patient
from rest_framework.parsers import JSONParser
from rest_framework import status 
# Create your views here.

def register(request):
    return render(request,"patient.html")


@csrf_exempt
def patient(request):
    if(request.method=="POST"):
        mydic=JSONParser().parse(request)
        patient_serialize=patientSerializer(data=mydic)
        if (patient_serialize.is_valid()):
            patient_serialize.save()
            return JsonResponse(patient_serialize.data)
        else:
            return HttpResponse("error in serilazation")

    else:
        return HttpResponse("sucess")


@csrf_exempt
def patientlist(request):
    if(request.method=="GET"):
        patients=Patient.objects.all()
        patient_serializer=patientSerializer(patients,many=True)
        return JsonResponse(patient_serializer.data,safe=False)

@csrf_exempt
def mypatients(request,fetchid):
    try:
        patient1=Patient.objects.get(id=fetchid)
        if(request.method=="GET"):
            patient_serializer=patientSerializer(patient1)
            return JsonResponse(patient_serializer.data,safe=False)

        if(request.method=="DELETE"):
            patient1.delete()
            return HttpResponse("Deleted",status=status)

        if(request.method=="PUT"):
            mydic=JSONParser().parse(request)
            patient_serialize=patientSerializer(patient1,data=mydic)
            if (patient_serialize.is_valid()):
                patient_serialize.save()
                return JsonResponse(patient_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(patient_serialize.errors)

    except Patient.DoesNotExist:
        return HttpResponse("invalid syntax",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def mypatient1(request,fetchcode):
    try:
        patient1=Patient.objects.get(patientcode=fetchcode)
        if(request.method=="GET"):
            patient_serializer=patientSerializer(patient1)
            return JsonResponse(patient_serializer.data,safe=False)

    except Patient.DoesNotExist:
        return HttpResponse("invalid syntax")