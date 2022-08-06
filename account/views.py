
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
		data.update(serializer.data)
		data['age_in_days'] = account.age_in_days
		data['age_in_months'] = int(account.age_in_days/30)
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
			serial_pass=serializer.data.get("password")
			pass_word = Account.objects.get(email=serializer.data.get('email')).password
			if serial_pass == pass_word:
					account = Account.objects.get(email=serializer.data.get('email'))
					user_datail = RegistrationSerializer(account)

					data={'id':account.id}
					data.update(user_datail.data)
					data['age_in_days'] = account.age_in_days
					data['age_in_months'] = int(account.age_in_days/30)

					res={'response' : 'login successfully',
						 'data' : data }

					return JsonResponse(res)

			else :
					return JsonResponse({'response':'password is not correct'},status=400)

		except Account.DoesNotExist:
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

class Profile_View(viewsets.ViewSet):
	queryset = Account.objects.all().filter()
	serializer_class = ProfileSerializer
	parser_classes = (MultiPartParser, FormParser)

	def get(self , request , id= None ):
		user = Account.objects.get(id=id)
		image = ProfileSerializer(user )
		user_datail = RegistrationSerializer(user)

		data={'id':user.id}
		data.update(user_datail.data)
		data['age_in_days'] = user.age_in_days
		data['age_in_months'] = int(user.age_in_days/30)
		data['image'] = image.data['image']

		res={'response' :'ok','data' : data }

		return JsonResponse( res)

	def post(self , request , id=None):
		image = request.data['image']
		user = Account.objects.get(id=id)
		user.image = image
		user.save()
		return JsonResponse({'response':'image saved'})

	def profile_pic(self , request , id= None ):
		user = Account.objects.get(id=id)
		image = ProfileSerializer(user )

		return JsonResponse({'response': 'ok', 'image' : image.data['image']})
