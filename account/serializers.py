from rest_framework import serializers

from account.models import Account
from rest_framework.serializers import Serializer, FileField

    
class UploadSerializer(Serializer):
    image = FileField()
    class Meta:
        fields = ['image']

class ProfileSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(required=True)

    class Meta:
        model = Account
        fields = ('image',)

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
            'age_in_days',
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
# email
# password
# babyname
# father
# mother
# address
# birth
# age_in_days
# pragnancyduration
# gender
# cm_length
# kg_weight
# arrangement_among_siblings
# image