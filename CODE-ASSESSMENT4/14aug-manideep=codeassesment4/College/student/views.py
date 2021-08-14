from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here. 

@csrf_exempt
def Stud(request):
    if(request.method=="POST"):
        getname=request.POST.get("name")
        getadmission=request.POST.get("admisssion")
        getrolno=request.POST.get("rolno")
        getcollege=request.POST.get("college")
        getparentname=request.POST.get("parentname")
        mydict1={"name":getname,"admissionno":getadmission,"rollno":getrolno,"college":getcollege,"parentname":getparentname}
        result1=json.dumps(mydict1)
        return HttpResponse(result1)


    else:
        return HttpResponse("no get method allowed")
