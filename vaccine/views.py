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
        age_related = int(b.age_in_days/30) 

        lis = []; i=0

        s_v = B_V.objects.all().filter(baby= b).filter(vaccine__static_duration=age_related)

        for s in s_v:
            lis.append({
               'id'             : s.id,       
               'vaccine_name'   : s.vaccine.vacine_name , 
               'dose_num'       : s.vaccine.dose_num,
               'month': age_related+1,
               'taken'          : s.taken,
               'dead_line'      : s.dead_line
               })

        return Response({'response':'ok','vaccines':lis})

from django.db.models import Q

@api_view(['GET'])
def check_vaccine_view(request, baby_id , vaccin_id ):
   if request.method == 'GET': 
      
      baby = Account.objects.get(id=baby_id)
      b = B_V.objects.get(Q(baby=baby) &  Q(id=vaccin_id))
      b.taken = 1-b.taken
      b.save()

      return Response({"check":bool(b.taken)},status=200)