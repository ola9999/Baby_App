from rest_framework import serializers 
from rest_framework.serializers import Serializer, FileField
from app.models import *

from drf_extra_fields.fields import Base64ImageField