from django.shortcuts import render
from account.serializers import (RegistrationSerializer,
								 SignInSerializer,
								 )


from rest_framework import status	
from django.http.response import JsonResponse
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.response import Response
from rest_framework.decorators import   api_view
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status  

from account.models import Account
from vaccine.models import B_V,All_Vaccines

@api_view(['POST'])
def registration_view(request):

	# request =JSONParser().parse(request.data)
	if request.method == 'POST':

		serializer = RegistrationSerializer(data=request.data)

		if serializer.is_valid():
			account = serializer.save()


		else:
			data = serializer.errors
			 
			return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)
		
		# return JsonResponse({'response':'successfully registered new user.'})
		return JsonResponse(serializer.data , status=200)


@api_view(['POST'])
def sign_in_view(request):

	if request.method == 'POST':
		# request_data =JSONParser().parse(request)
		serializer = SignInSerializer(data=request.data)

		print(serializer.is_valid())

		try:
			serial_email = serializer.data.get("email")
			print(111) 
		except Account.DoesNotExist:
			print(222)
			return  JsonResponse({'response': 'This user does not exist'})

	
		serial_pass=serializer.data.get("password")
		pass_word = Account.objects.get(email=serializer.data.get('email')).password


		if serial_pass == pass_word:
				# return JsonResponse({'response' : 'login successfully'})

				id = Account.objects.get(email=serializer.data.get('email')).id
				data={'id':id}
				data.update(serializer.data)

				return JsonResponse(data)

		else :
				return JsonResponse({'response':'password is not correct'},status=400)
	