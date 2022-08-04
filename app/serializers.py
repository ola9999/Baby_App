from rest_framework import serializers 
from rest_framework.serializers import Serializer, FileField
from app.models import *

from drf_extra_fields.fields import Base64ImageField


class LallubySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lalluby
        fields = ('song_name','file')


class AlbumSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(required=True)

    class Meta:
        model = Album
        fields = ('image',)