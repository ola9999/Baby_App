from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from account.views import *

urlpatterns = [

    path('register', registration_view, name='registration_view'),
    path('signin', sign_in_view, name='sign_in_view'),
    path('profile/<int:pk>', Profile_View.as_view(), name='Profile_View'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)