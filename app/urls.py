from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from app.views import *
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('illnesse/<str:ch>', ill_treat_search_view, name='illnesse'),
    path('feed/<int:age>', feed_view, name='feed'), #age in monthes
    path('sleep/<int:age>', sleep_view, name='sleep'),#age in monthes
    path('lalluby', lalluby_view, name='lalluby'),
    path('tips', tips_view, name='tips'),
    path('<int:pk>/album', Album_View.as_view(), name='Album_View'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
