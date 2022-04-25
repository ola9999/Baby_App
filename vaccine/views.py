# from django.shortcuts import render
# from django.http.response import JsonResponse
# from rest_framework.response import Response
# from rest_framework.decorators import   api_view
# from datetime import datetime, timedelta #2022-04-23
# from vaccine.models import *
# from vaccine.serializers import VaccineSerializer


# from rest_framework import status

# @api_view(['GET'])
# def vaccines_view(request):

#      if request.method == 'GET':
#         data = Vaccine.objects.all()
#         serializer = VaccineSerializer(data, many=True)
#         serializer.is_valid(raise_exception=True)
        
#         return Response(serializer.data)