from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from app.views import *
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('lalluby', LallubyViewSet, basename="lalluby")

urlpatterns = [
    path('', all_views_view, name='all_views_view'),

    path('illnesse/<str:ch>', ill_treat_search_view, name='illnesse'),
    path('feed/<int:id>', feed_view, name='feed'), #age in monthes
    path('sleep/<int:id>', sleep_view, name='sleep'),#age in monthes
    # path('lalluby', lalluby_view, name='lalluby'),
    path('tips/<int:id>', tips_view, name='tips'),
    path('album/<int:id>', Album_View.as_view(), name='Album_View'),

    path('', include(router.urls)),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
