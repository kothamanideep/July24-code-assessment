from django.urls import path,include
from.import views

urlpatterns=[
    path('fact/', views.fac, name='fac'),
]