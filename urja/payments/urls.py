from django.contrib import admin
from django.urls import path,include
from .views import *

app_name='payments'

urlpatterns = [
    path('report', paymentreport,name='paymentreport'),

]