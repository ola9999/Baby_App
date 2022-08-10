from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from app.views import *
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('album', Album_View, basename="album")
router.register('send_lalluby', LallubyViewSet, basename="send_lalluby")

urlpatterns = [
    

    path('album/<int:id>', Album_View.as_view({'post': 'post'}) , name='Album_View'),
    path('album/<int:id>', Album_View.as_view({'get': 'get'}) , name='Album_View'),

    path('illnesse/<str:ch>', ill_treat_search_view, name='illnesse'),
    path('feed/<int:id>', feed_view, name='feed'), #age in monthes
    path('sleep/<int:id>', sleep_view, name='sleep'),#age in monthes
    path('tips/<int:id>', tips_view, name='tips'),
    path('get_lalluby', lall, name='lalluby'),

    path('all', all_views_view, name='all_views_view'),

    path('', include(router.urls)),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
