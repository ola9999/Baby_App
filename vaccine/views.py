from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import   api_view
from datetime import datetime, timedelta #2022-04-23
from vaccine.models import  All_Vaccines,B_V
from account.models import Account

from rest_framework import status

@api_view(['GET'])
def vaccines_view(request, id, age ):

     if request.method == 'GET': 
        
        b = Account.objects.get(id=id)
        v_b = B_V.objects.all().filter(baby= b).filter(vaccine__static_duration = age)
        
        data = {}
        lis = []
      #   data ['baby']           = {'baby_name'  : b.babyname , 
      #                                  'baby_birth' : b.birth } 
        for v in v_b:

            print('************')
            dic= {}
            dic[v.vaccine.static_duration+1 ]={
                  'vaccine_name'   : v.vaccine.vacine_name , 
                  'dose_num'       : v.vaccine.dose_num,
               #    'static_duration': v.vaccine.static_duration,
                  'taken'          : v.taken,
                  'dead_line'      : v.dead_line
                  } 
            print( dic )


            lis.append(dic) 

        print(5)
        data['data']=lis
        print( lis )
        
        return Response(data)