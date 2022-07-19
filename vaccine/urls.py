from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from vaccine.views import *

urlpatterns = [

    path('vaccine/<int:id>', vaccines_view, name='vaccines'),# account id 
    path('check_vaccine/<int:baby_id>/<int:vaccin_id>', check_vaccine_view, name='check_vaccine')# 
    
]