from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import   api_view
from datetime import datetime, timedelta #2022-04-23
from vaccine.models import  All_Vaccines,B_V
from account.models import Account

from rest_framework import status

@api_view(['GET'])
def vaccines_view(request, id ):

     if request.method == 'GET': 
        
        b = Account.objects.get(id=id)
        v_b = B_V.objects.all().filter(baby= b)
        
        data = {}
        dic= {}
        lis = []

        for v in v_b:
            dic = {'baby'           : {'baby_name'  : b.babyname , 
                                       'baby_birth' : b.birth } ,
                    'vaccine':{
                   'vaccine_name'   : v.vaccine.vacine_name , 
                   'dose_num'       : v.vaccine.dose_num,
                   'static_duration': v.vaccine.static_duration,
                   'taken'          : v.taken,
                   'dead_line'      : v.dead_line}
                   } 

            lis.append(dic)

        print(5)
        
        return Response({'data':lis})