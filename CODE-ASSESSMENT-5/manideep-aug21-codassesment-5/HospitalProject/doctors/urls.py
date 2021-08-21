from django.urls import path,include
from.import views
urlpatterns=[
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path("dcode/<fetchcode>",views.mydoctor1,name="mydoctor1"),
    path("add/",views.doctor,name="doctor"),
    path("viewall/",views.doctorlist,name="doctorlist"),
    path("view/<fetchid>",views.mydoctors,name="mydoctors"),

]