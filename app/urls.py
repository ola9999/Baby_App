from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from app.views import *
from rest_framework import routers
from .views import UploadViewSet
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'upload', UploadViewSet, basename="upload")


urlpatterns = [

    path('illnesse/<str:ch>', ill_treat_search_view, name='illnesse'),
    path('feed/<int:age>', feed_view, name='feed'), #age in monthes
    path('sleep/<int:age>', sleep_view, name='sleep'),#age in monthes
    path('lalluby', lalluby_view, name='lalluby'),
    path('tips', tips_view, name='tips'),
    path('postAlbum', post_album_view, name='upload Album'),
    path('getAlbum/<int:id>', get_album_view, name='get Album'),

    path('', include(router.urls)),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
