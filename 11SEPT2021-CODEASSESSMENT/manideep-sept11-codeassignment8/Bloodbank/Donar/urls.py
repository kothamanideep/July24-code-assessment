from django.urls import path,include
from.import views
urlpatterns=[
    path("register/",views.register,name="register"),
    path("viewdonar/",views.viewdonar,name="viewdoanr"),
    path("update/",views.updatedonar,name="updatedonar"),
    path("search/",views.search,name="search"),
    path("adddonar/",views.donar,name="donar"),
    path("viewdonars/",views.donarlist,name="donarlist"),
    path("viewgroup/<fetchid>",views.mydonars,name="mydonars"),
    path('login/', views.loginview, name='loginview'),
    path('logincheck/', views.login_check, name='login_check'),
    path('updatesearch/',views.updatesearchapi,name='updatesearchapi'),
    path('updateApi/',views.update_data_read,name='update_data_read'),
]