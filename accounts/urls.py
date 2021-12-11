from django.urls import path
from .views import registerEmployeeView,loginEmployeeView,logout_view


urlpatterns = [

    path('register/',registerEmployeeView,name='register-employee'),
    path('login/',loginEmployeeView,name='login-employee'),
    path('logout/',logout_view,name='logout-employee'),
]