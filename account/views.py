
from account.serializers import *
from datetime import  timedelta,date

from rest_framework import status	
from django.http.response import JsonResponse
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.response import Response
from rest_framework.decorators import   api_view
from django.core.exceptions import ObjectDoesNotExist

# from rest_framework.response import Response

from account.models import Account
from vaccine.models import B_V,All_Vaccines

@api_view(['POST'])
def registration_view(request):
	
	if request.method == 'POST':


		serializer = RegistrationSerializer(data=request.data)

		if serializer.is_valid():
			account = serializer.save()


		else:
			data = serializer.errors
			 
			return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)

		account = Account.objects.get(email=serializer.data.get('email'))

		data={'id':account.id}
		data['age_in_days'] = account.age_in_days
		data['age_in_months'] = int(account.age_in_days/30)
		data.update(serializer.data)
		res={'response' : 'successfully registered new user',
				'data' : data }

		return JsonResponse(res, status=200)

@api_view(['POST'])
def sign_in_view(request):

	if request.method == 'POST':

		serializer = SignInSerializer(data=request.data)

		print(serializer.is_valid())

		try:
			serial_email = serializer.data.get("email")
			print(111) 
			serial_pass=serializer.data.get("password")
			pass_word = Account.objects.get(email=serializer.data.get('email')).password
			if serial_pass == pass_word:
					account = Account.objects.get(email=serializer.data.get('email'))

					data={
						'id':account.id,
						"babyname":account.babyname,
						"father":account.father,
						"mother":account.mother,
						"address":account.address,
						"birth": account.birth,
						"pragnancyduration":account.pragnancyduration,
						"gender":account.gender,
						"cm_length":account.cm_length,
						"kg_weight":account.kg_weight,
						"arrangement_among_siblings":account.arrangement_among_siblings,
						"email":serializer.data['email']
						}
					res={'response' : 'login successfully',
						 'data' : data }

					return JsonResponse(res)

			else :
					return JsonResponse({'response':'password is not correct'},status=400)

		except Account.DoesNotExist:
			print(222)
			return  JsonResponse({'response': 'This user does not exist'})
	
# @api_view(['GET'])
# def user_detail_view(request,id):

# 	if request.method == 'GET':

# 		account = Account.objects.get(id=id)
# 		serializer = RegistrationSerializer(account)
# 		print (serializer.data)

# 		data={'id':account.id}
# 		data['age_in_days'] = account.age_in_days
# 		data['age_in_months'] = int(account.age_in_days/30)
# 		data.update(serializer.data)

# 		res={'response' :'ok','data' : data }

#
# 		return  JsonResponse(res)
		

from rest_framework.parsers import MultiPartParser, FormParser ,FileUploadParser
from rest_framework import viewsets
from rest_framework.viewsets import ViewSet
