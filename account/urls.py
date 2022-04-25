from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from account.views import *

urlpatterns = [

    path('register', registration_view, name='registration_view'),
    path('signin', sign_in_view, name='sign_in_view'),
    
    # path('<int:pk>/profile', profile_View.as_view(), name='profile_view'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)