from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from app.views import *

urlpatterns = [

    path('illnesse/<str:ch>', ill_treat_search_view, name='illnesse'),
    path('feed/<int:age>', feed_view, name='feed'), #age in monthes
    path('sleep/<int:age>', sleep_view, name='sleep'),#age in monthes
    path('lalluby', lalluby_view, name='lalluby'),
    path('tips', tips_view, name='tips'),
    path('Album/<int:id>', Album_view, name='Album'),

]