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
        data = {};lis = []; vac={}; i=0
        v_b = B_V.objects.all().filter(baby= b)

        for v in v_b:
            s_v = B_V.objects.all().filter(baby= b).filter(vaccine__static_duration=v.vaccine.static_duration)
            dic={};i=0
            for s in s_v:
               dic[i]={
                  'vaccine_name'   : s.vaccine.vacine_name , 
                  'dose_num'       : s.vaccine.dose_num,
                  # 'static_duration': v.vaccine.static_duration,
                  'taken'          : s.taken,
                  'dead_line'      : s.dead_line
                  }
               i=+1

            data[v.vaccine.static_duration+1 ]=dic

            print(data)
        return Response(data)
            
            # lis.append(dic) 
            # {1 : {0:{'abcabc':'cdecde'},
            #       1:{'efg':'hij'}, 
            #       2:{'klmn':'opq'},
            #       3:{'rstu':'vwx'}
            #       }
            #  3 : {0:{'abcabc':'cdecde'},
            #       1:{'efg':'hij'}, 
            #       }}
            #  4 : {0:{'abcabc':'cdecde'},
            #       1:{'efg':'hij'}, 
            #       2:{'klmn':'opq'},
            #       }
                  # }
      #   data['data']=lis
      #   print( lis )
        

      #   {0: {0: {'vaccine_name': 'Hepatities B'},
      #          1: {'vaccine_name': 'BCG'}, 
      #         2: {'vaccine_name': 'Polio'}}, 
      #    2: {0: {'vaccine_name': 'DTP'}, 
      #          1: {'vaccine_name': 'Hepatities B'}, 
      #          2: {'vaccine_name': 'Oral Polio'}},
      #    4: {0: {'vaccine_name': 'DTP'},
      #        1: {'vaccine_name': 'Oral Polio'}},
      #    1: {0: {'vaccine_name': 'k'}}}