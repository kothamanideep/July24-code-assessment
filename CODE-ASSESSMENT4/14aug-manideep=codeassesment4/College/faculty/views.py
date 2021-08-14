from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here. 

@csrf_exempt
def fac(request):
    if(request.method=="POST"):
        getname=request.POST.get("name")
        getadress=request.POST.get("adress")
        getdepartment=request.POST.get("department")
        getcollege=request.POST.get("college")
        mydict={"name":getname,"adress":getadress,"department":getdepartment,"college":getcollege}
        result=json.dumps(mydict)
        return HttpResponse(result)


    else:
        return HttpResponse("no get method allowed")