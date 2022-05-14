from rest_framework import serializers 
from rest_framework.serializers import Serializer, FileField
from app.models import *

# class RegistrationSerializer(serializers.ModelSerializer):
#     # profile = ProfileSerializer(read_only=True)

#     class Meta:
#         model = Account
#         fields =[
#             'email',
#             'password',
#             'babyname',
#             'father',
#             'mother',
#             'address',
#             'birth',
#             'pragnancyduration',
#             'gender',
#             'cm_length',
#             'kg_weight',
#             'arrangement_among_siblings',
#             ]

class UploadSerializer(Serializer):
    file_uploaded = FileField()
    class Meta:
        fields = ['file_uploaded']

# class FileSerializer(ModelSerializer):
    
#     class Meta:
#         model = Album
#         fields = ('image')