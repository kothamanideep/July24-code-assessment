from django.urls import path,include
from.import views
urlpatterns=[
    path('',views.register,name="register"),
    path("pcode/<fetchcode>",views.mypatient1,name="mypatient1"),
    path("add/",views.patient,name="patient"),
    path("viewall/",views.patientlist,name="patientlist"),
    path("view/<fetchid>",views.mypatients,name="mypatients"),

]