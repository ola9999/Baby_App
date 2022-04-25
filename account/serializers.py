from rest_framework import serializers

from account.models import Account

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
        fields = ['email', 'password' ,]#, 'password2']#' __all__ '#






#, 'password2']#' __all__ '#

#	password2 				= serializers.CharField( max_length=60)
#	password 				= serializers.CharField( max_length=60)

	
