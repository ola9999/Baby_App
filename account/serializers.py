from rest_framework import serializers

from account.models import Account
from rest_framework.serializers import Serializer, FileField

class Pic(object):
    def __init__(self, image):
        self.image = image

class PicSerializer(serializers.Serializer):
    # initialize fields
    image = serializers.ImageField()


    
class UploadSerializer(Serializer):
    file_uploaded = FileField()
    class Meta:
        fields = ['file_uploaded']


class RegistrationSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Account
        fields =[
            'email',
            'password',
            'babyname',
            'father',
            'mother',
            'address',
            'birth',
            'pragnancyduration',
            'gender',
            'cm_length',
            'kg_weight',
            'arrangement_among_siblings',
            ]


class SignInSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['email', 'password' ,]
	
class BabySerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields =[
            'babyname',
            'birth',
            ]
