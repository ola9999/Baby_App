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
               'vaccine_name'   : s.vaccine.vacine_name , 
               'dose_num'       : s.vaccine.dose_num,
               'month': age_related+1,
               'taken'          : s.taken,
               'dead_line'      : s.dead_line
               })

        return Response(lis)
            
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