from django.shortcuts import render
from account.serializers import *
from datetime import  timedelta,date

from rest_framework import status	
from django.http.response import JsonResponse
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.response import Response
from rest_framework.decorators import   api_view
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status  
from rest_framework.response import Response

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
		# return JsonResponse({'response':'successfully registered new user.'})
		return Response(data , status=200)


@api_view(['POST'])
def sign_in_view(request):

	if request.method == 'POST':

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

				# id = Account.objects.get(email=serializer.data.get('email')).id
				# data={'id':id}
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

				return JsonResponse(data)

		else :
				return JsonResponse({'response':'password is not correct'},status=400)
	
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from PIL import Image

class Profile_View(APIView):
	parser_classes = (FileUploadParser,)
	serializer_class = UploadSerializer

	def get (self ,request , pk ):
		file = Account.objects.get(id=pk).image
		# image_file = Image.open(file)
		# import pdb; pdb.set_trace()
		# print(file)
		# create a object of type Pic
		obj = Pic( file)
		serializer = PicSerializer(obj)
		return Response({"file": serializer.data})
		
	def post(self ,request , pk ):
		file = request.data['file']
		# import pdb; pdb.set_trace()
		# print(file)
		if file:
			user =Account.objects.get(id=pk)
			user.image = file
			user.save()
			img =Account.objects.get(id=pk).image
			obj = Pic( img)
			serializer = PicSerializer(obj)
			# img = Image.open(file)
			# return Response({"mode": img.mode, "size": img.size, "format": img.format})
			return Response({"file":serializer.data})
		else : 
			return Response({'massege':'error'} , status=400)

# return Response({"mode": img.mode, "size": img.size, "format": img.format})
# from rest_framework import viewsets
# from account.serializers import *
# from rest_framework.viewsets import ViewSet

# class UploadViewSet(viewsets.ModelViewSet):
#     queryset = Account.objects.all()
#     serializer_class = UploadSerializer

# 	@action(methods=["get"], detail=True)
# 	def approvedRequests(self, request, employee_id)

