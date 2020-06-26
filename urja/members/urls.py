from django.contrib import admin
from django.urls import path
from .views import *

app_name='members'

urlpatterns = [
	path('home', home,name='home'),
    path('add/', insertmember,name='addmember'),
    path('members/',getallmembers,name='getallmembers'),
    path('deletemembers/<int:pk>/',deletemembers,name='deletemembers'),
    path('<int:pk>',editmembers,name='editmembers'),
    path('login',loginmember,name='loginmember'),
    path('memberdata',memberdata,name='memberdata'),
    path('logout',logoutmember,name='logoutmember'),
    

]
