from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from account.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('profile', Profile_View, basename="album")

urlpatterns = [

    path('register', registration_view, name='registration_view'),
    path('signin', sign_in_view, name='sign_in_view'),
    path('profile/<int:id>', Profile_View.as_view({'post': 'post'}), name='Profile_View'),
    path('profile/<int:id>', Profile_View.as_view({'get': 'get'}), name='Profile_View'),
    path('profile_pic/<int:id>', Profile_View.as_view({'get': 'profile_pic'}), name='Profile_View'),

    # path('', include(router.urls)),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)