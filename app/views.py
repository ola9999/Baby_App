from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework.decorators import   api_view
from app.models import *
from rest_framework import status


@api_view(['GET'])
def all_views_view(request):#age in monthes

    pre="http://127.0.0.1:8000/"
    data = {"post":[
            pre+"signin" , 
            pre+"register",
                    ] ,
            "get":[
            pre+"admin",  
            pre+"profile/1",
            pre+'profile_pic/1',
            '........................',
            pre+"vaccine/<int:id>",
            pre+"vaccine/1",

            pre+"check_vaccine/1/96",
            '........................',

            pre+"feed/1",
            pre+"sleep/1",
            pre+"tips/1",
            
            pre+"illnesse/<str:ch>",
            pre+"illnesse/ا",
            '........................',
            pre+"get_lalluby",
            ],

            "get&post":[     
            "Content-Disposition:attachment; filename=sticker.png",
            '........................',
            pre+"profile/<int:id>",
            pre+"album/<int:id>",
            pre+"album/1",
            '........................',
            pre+'send_lalluby/',]}

    return Response(data)    


@api_view(['GET'])
def feed_view(request, id ):#age in monthes # changed
    
    if request.method == 'GET': 

        age_related = int((Account.objects.get(id = id).age_in_days)/30) +1
        dic={}
        food = Feed.objects.all().filter(age_related = age_related)

        for f in food:
            dic={
                'Breast milk':[s.food_name for s in food.filter(food_type='Breast milk')],
                'Formula milk':[s.food_name for s in food.filter(food_type='Formula milk')],
                'Water':[s.food_name for s in food.filter(food_type='Water')],
                'Fruits':[s.food_name for s in food.filter(food_type='Fruits')],
                'Vegetables':[s.food_name for s in food.filter(food_type='Vegetables')],
                'Cyrbohedats':[s.food_name for s in food.filter(food_type='Cyrbohedats')],
                'Cremy':[s.food_name for s in food.filter(food_type='Cremy')]
            }

        data=[dic]
        return JsonResponse({'response':'ok',"food":data})
        

@api_view(['GET'])
def sleep_view(request, id): # has changed

     if request.method == 'GET': 
        
        age_related = int((Account.objects.get(id = id).age_in_days)/30) +1
        sleep = Sleep.objects.all().filter(age_related = age_related )
        lis=[s.sleep_duration for s in sleep.filter(age_related=age_related)]
        
        return JsonResponse({'response':'ok','sleep':lis[0]})


from django.db.models import Q
@api_view(['GET'])
def tips_view(request, id):# has changed

     if request.method == 'GET': 

        age_related = int((Account.objects.get(id = id).age_in_days)/30) +1
        tip = Tips.objects.all().filter(age_related = age_related )
        lis=[]

        for t in tip:
            lis.append({'title':t.title,
                        'tip'  :t.tip})

        return JsonResponse({'response':'ok','tips':lis})

from django.db.models import Q

@api_view(['GET'])
def ill_treat_search_view(request, ch ): # search ills start with {ch} 

     if request.method == 'GET':
        
        illnesse = Illnesse.objects.all().filter( Q(ill_name__startswith=ch.lower())|  Q(ill_name__startswith=ch.upper()))

        lis=[];i=0
        for l in illnesse :
            
            lis.append( {
                  'ill_name'       : l.ill_name ,
                  'treats'     : [t.treat_name for t in l.treat.all()]
                  } )
            i+=1

        return JsonResponse({'response':'ok',"Illnesses":lis})

from rest_framework.parsers import MultiPartParser, FormParser ,FileUploadParser
from rest_framework.views import APIView
from rest_framework import viewsets
from app.serializers import *
from rest_framework.viewsets import ViewSet
import requests
class Album_View(viewsets.ModelViewSet):
    queryset =  Album.objects.all()
    serializer_class = AlbumSerializer
    parser_classes = (MultiPartParser, FormParser)


    def get (self ,request , id= None ):
        baby = Account.objects.get(id=id)
        albums = Album.objects.all().filter(baby = baby)   
        serializer = AlbumSerializer(albums, many = True)
        lis=[]
        for s in serializer.data:
            lis.append(s['image'])
        return JsonResponse({'response':'ok','images' : lis})

    def post(self, request, id=None ):
        print(request.data)
        user = Account.objects.get(id=id)
        albums = Album(baby =user , image =request.data['image'] )
        albums.save()
        # response = requests.get('http://127.0.0.1:8000/album/'+str(id))
        # response = response.json()
        return JsonResponse({'response': 'image saved'})#, 'images':response['images']})


class LallubyViewSet(viewsets.ModelViewSet):
    queryset = Lalluby.objects.all()
    serializer_class = LallubySerializer

def lall(request):
    #pull data from third party rest api
    response = requests.get('http://127.0.0.1:8000/send_lalluby/')
    songs = response.json()
    return JsonResponse({'response':'ok',"tracks":songs})
