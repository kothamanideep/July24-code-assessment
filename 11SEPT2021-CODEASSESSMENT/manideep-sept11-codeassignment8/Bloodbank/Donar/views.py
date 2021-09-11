from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from Donar.serializers import donarSerializer
from Donar.models import Donar
from rest_framework.parsers import JSONParser
from rest_framework import status 
import requests
# Create your views here.

def register(request):
    return render(request,"register.html")

def loginview(request):
    return render(request, 'login.html')

def search(request):
    return render(request,"search.html")

def updatedonar(request):
    return render(request,"update.html")



def viewdonar(request):
    fetchdata=requests.get("http://127.0.0.1:8000/Donar/viewdonars/").json()
    return render(request,"viewall.html",{"data":fetchdata})

@csrf_exempt
def donar(request):
    if(request.method=="POST"):
        # mydic=JSONParser().parse(request)
        donar_serialize=donarSerializer(data=request.POST)
        if (donar_serialize.is_valid()):
            donar_serialize.save()
            return JsonResponse(donar_serialize.data)
        else:
            return HttpResponse("error in serilazation")

    else:
        return HttpResponse("sucess")


@csrf_exempt
def donarlist(request):
    if(request.method=="GET"):
        donars=Donar.objects.all()
        donar_serializer=donarSerializer(donars,many=True)
        return JsonResponse(donar_serializer.data,safe=False)

@csrf_exempt
def mydonars(request,fetchid):
    try:
        donar1=Donar.objects.get(id=fetchid)
        if(request.method=="GET"):
            donar_serializer=donarSerializer(donar1)
            return JsonResponse(donar_serializer.data,safe=False)


        if(request.method=="PUT"):
            mydic=JSONParser().parse(request)
            donar_serialize=donarSerializer(donar1,data=mydic)
            if (donar_serialize.is_valid()):
                donar_serialize.save()
                return JsonResponse(donar_serialize.data)
            else:
                return JsonResponse(donar_serialize.errors)
    except Donar.DoesNotExist:
        return HttpResponse("invalid syntax")

@csrf_exempt
def updatesearchapi(request):
    try:
        getname=request.POST.get("donarname")
        getdonar=Donar.objects.filter(donarname=getname)
        donar_serializer=donarSerializer(getdonar,many=True)
        return render(request,"update.html",{"data":donar_serializer.data})
        # return JsonResponse(event_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Donar.DoesNotExist:
        return HttpResponse("Invalid title",status=status.HTTP_404_NOT_FOUND)    
    
    except:
        return HttpResponse("something went wrong")


@csrf_exempt
def update_data_read(request):
    getnewid=request.POST.get("newid")

    getnewbloodgroup=request.POST.get("newbloodgroup")
    getnewname=request.POST.get("newname")
    getnewaddress=request.POST.get("newaddress")
    getnewmobilenumber=request.POST.get("newmobilenumber")
    getnewusername=request.POST.get("newusername")
    getnewpassword=request.POST.get("newpassword")
    mydata={'bloodgroup':getnewbloodgroup,'donarname':getnewname,'address':getnewaddress,'mobilenumber':getnewmobilenumber,'username':getnewusername,'password':getnewpassword}
    jsondata=json.dumps(mydata)
    Apilink="http://127.0.0.1:8000/Donar/view/"+getnewid
    requests.put(Apilink,data=jsondata)
    return HttpResponse("data has updated sucessfully")



@csrf_exempt
def login_check(request):
    try:
        getUsername = request.POST.get("username")
        getPassword = request.POST.get("password")
        getUsers = Donar.objects.filter(username=getUsername, password=getPassword)
        donar_serialiser = donarSerializer(getUsers, many=True)
        print(donar_serialiser.data)
        if (donar_serialiser.data):
            for i in donar_serialiser.data:
                getId = i["id"]
                # getName = i["name"]
                getUsername = i["username"]
                getPassword = i["password"]

            request.session['uid'] = getId
            request.session['uusername'] = getUsername
            request.session['upassword'] = getPassword
            return render(request,"viewall.html")
        else:
            return HttpResponse("Invalid details")     


           
            
            
    except Donar.DoesNotExist:
        return HttpResponse("Invalid Username or Password ", status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something went wrong")


