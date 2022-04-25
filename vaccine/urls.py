from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from vaccine.views import *

urlpatterns = [

    path('vaccines', vaccines_view, name='vaccines')

]