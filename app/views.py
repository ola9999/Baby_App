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

            pre+"illnesse/<str:ch>",
            pre+"illnesse/i",

            pre+"feed",
            pre+"sleep",
            pre+"tips",
            pre+"lalluby",
            ],
            "get&post":[     
            "Content-Disposition:attachment; filename=sticker.png",
            pre+"profile/<int:id>",
            pre+"album/<int:id>",]}

    return Response(data)    


@api_view(['GET'])
def feed_view(request):#age in monthes
    
    if request.method == 'GET': 
        
        feed = Feed.objects.all()
        data = {}
        for f in feed :
            s_v = Feed.objects.all().filter(age_related = f.age_related )
            
            dic= {}; i=0
            lis = [] 
            for s in s_v:
                obj =  s.food_icon
                obj = Pic( obj )
                serializer = PicSerializer(obj)
                

                lis.append( {
                #   'age_related'     : s.age_related,
                  'food_name'       : s.food_name , 
                  'food_type'       : s.food_type,
                  'food_icon'          :serializer.data['image'] 
                  } )

            data[f.age_related]=lis
            
        return Response(data)
        

@api_view(['GET'])
def sleep_view(request):

     if request.method == 'GET': 
        
        sleep = Sleep.objects.all()
        
        data = {} 
        for sp in sleep :
            s_v = sleep.filter(age_related = sp.age_related )
            dic= {}; i=0; lis=[]
            # for s in s_v:
            #     lis.append( {
            #         'sleep_duration'       : s.sleep_duration 
            #         #  ,'age_related'     : s.age_related
            #         } )
            #     i= i+1
            # data[sp.age_related]=dic
            dic={
                'sleep_duration'       : sp.sleep_duration 
                #  ,'age_related'     : s.age_related
                }
            

            data[sp.age_related]=dic

        return Response(data)


@api_view(['GET'])
def tips_view(request):

     if request.method == 'GET': 
        
        tip = Tips.objects.all()
        data = {} ; i=0 ; lis=[]

        for t in tip :
            s_v = Tips.objects.all().filter(age_related = t.age_related )
            
            lis.append(t.tip)
            for s in s_v:
              data[t.age_related]=lis

        return Response(data)

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
