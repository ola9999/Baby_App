from rest_framework import serializers 
from rest_framework.serializers import Serializer, FileField
from app.models import *

from drf_extra_fields.fields import Base64ImageField

class Pic(object):
    def __init__(self, image):
        self.image = image

class PicSerializer(serializers.Serializer):
    # initialize fields
    image = serializers.ImageField()


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lalluby
        fields = ('song_name','file')