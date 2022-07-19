from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import   api_view
from app.models import *
from rest_framework import status
# from app.serializers import *
from PIL import Image


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

            pre+"vaccine/<int:id>",
            pre+"vaccine/1",

            pre+"check_vaccine/1/96",

            pre+"feed/1",
            pre+"sleep/1",
            pre+"tips/1",
            
            pre+"illnesse/<str:ch>",
            pre+"illnesse/ا",

            pre+"lalluby",
            ],
            "get&post":[     
            "Content-Disposition:attachment; filename=sticker.png",
            pre+"profile/<int:id>",
            pre+"album/<int:id>",]}

    return Response(data)    


@api_view(['GET'])
def feed_view(request, id ):#age in monthes # changed
    
    if request.method == 'GET': 
        
        # feed = Feed.objects.all()
        data = {}

        age_related = int((Account.objects.get(id = id).age_in_days)/30) +1

        s_v = Feed.objects.all().filter(age_related = age_related )

        lis = [] 
            
        dic= {}; i=0
        
        for s in s_v:
            obj =  s.food_icon
            obj = Pic( obj )
            serializer = PicSerializer(obj)
            print([s.food_name for s in s_v.filter(food_type=s.food_type)])

            dic[s.food_type]=[s.food_name for s in s_v.filter(food_type=s.food_type)]
                # 'month'     : s.age_related,
                # s.food_type       : [s.food_name for s in s_v.filter(food_type=s.food_type)]
                # 'food_type'       : s.food_type,
                # 'food_icon'       :serializer.data['image'] 
                # } )

        # lis.append(dic)
        return Response(dic)
        

@api_view(['GET'])
def sleep_view(request, id): # has changed

     if request.method == 'GET': 
        
        age_related = int((Account.objects.get(id = id).age_in_days)/30) +1

        sleep = Sleep.objects.all().filter(age_related = age_related )
        lis=[]
        for sp in sleep :

            lis.append({
                'sleep_duration'       : sp.sleep_duration 
                # ,'month'     : sp.age_related
                })

        return Response(lis)


from django.db.models import Q
@api_view(['GET'])
def tips_view(request, id):# has changed

     if request.method == 'GET': 

        # b = B_V.objects.get(Q(baby=baby) &  Q(id=vaccin_id)) 

        age_related = int((Account.objects.get(id = id).age_in_days)/30) +1

        tip = Tips.objects.all().filter(age_related = age_related )
        lis=[]

        for t in tip:
            # lis.append(t.tip)
            # data[t.age_related]=lis

            lis.append(t.tip)

        return Response({'tips':lis})

from django.db.models import Q

@api_view(['GET'])
def ill_treat_search_view(request, ch ): # search ills start with {ch} 

     if request.method == 'GET':
        
        illnesse = Illnesse.objects.all().filter( Q(ill_name__startswith=ch.lower())|  Q(ill_name__startswith=ch.upper()))

        data = {} ; dic= {}; i=0;j=0 ; lis=[]
        for l in illnesse :
            
            lis.append( {
                  'ill_name'       : l.ill_name ,
                  'treats'     : [t.treat_name for t in l.treat.all()]
                  } )
            # for t in l.treat.all():
            #     dic[j]=t.treat_name
            #     j+=1

            # data[i]['treats']= lis
            i+=1

        print(data)

        return Response({"Illnesses":lis})

from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from PIL import Image
from account.serializers import PicSerializer,Pic

class Album_View(APIView):
    parser_classes = (FileUploadParser,)

    def get (self ,request , id ):
        baby = Account.objects.get(id=id)
        albums = Album.objects.all().filter(baby = baby)   
        lis = []; i = 0
        for f in albums:
            obj = Pic( f.image )
            serializer = PicSerializer(obj)
            lis.append(serializer.data['image'])
            i=+1
        
        return Response({"data": lis})

    def post(self ,request , id ):
        file = request.data['file']
        user =Account.objects.get(id=id)

        if file:
            user.image = file
            user.save()
            img = Image.open(file)
            return Response({"response": "image saved" })
        else : 
            return Response({'response':'error'} , status=400)

from rest_framework import viewsets
from app.serializers import *
from rest_framework.viewsets import ViewSet

class LallubyViewSet(viewsets.ModelViewSet):
    queryset = Lalluby.objects.all()
    serializer_class = UploadSerializer

# @api_view(['GET'])
# def lalluby_view(request):

#      if request.method == 'GET': 
#         lalluby = Lalluby.objects.all()
#         data = {} ; lis = [] ; i=0
#         for l in lalluby :
#             dic= {}
#             data[i]={
#                   'song_name'       : l.song_name , 
#                 #   'file'     : l.file
#                   } 
#             i= i+1
#         return Response(data)
