from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import   api_view
from app.models import *
from rest_framework import status
from app.serializers import *

#شغلات نائصة بتخص الملفات 

@api_view(['GET'])
def feed_view(request, age ):#age in monthes

     if request.method == 'GET': 
        
        feed = Feed.objects.all().filter(age_related =age )
        
        data = {} ; lis = [] ; i=0
        for f in feed :
            dic= {}
            lis.append({
                  'age_related'     : f.age_related,
                  'food_name'       : f.food_name , 
                  'food_type'       : f.food_type
                #   'food_icon'          : f.food_icon,
                  } )
            i= i+1

        return Response({'data':lis})


@api_view(['GET'])
def sleep_view(request, age ):

     if request.method == 'GET': 
        
        sleep = Sleep.objects.all().filter(age_related = age )
        
        data = {} ; lis = [] ; i=0
        for s in sleep :
            dic= {}
            data[i]={
                  'sleep_duration'       : s.sleep_duration , 
                  'age_related'     : s.age_related
                  } 
            i= i+1

        return Response(data)

#شغلات نائصة بتخص الملفات 
@api_view(['GET'])
def lalluby_view(request):

     if request.method == 'GET': 
        
        lalluby = Lalluby.objects.all()
        
        data = {} ; lis = [] ; i=0
        for l in lalluby :
            dic= {}
            data[i]={
                  'song_name'       : l.song_name , 
                #   'file'     : l.file
                  } 
            i= i+1

        return Response(data)

@api_view(['GET'])
def tips_view(request):

     if request.method == 'GET': 
        
        tip = Tips.objects.all()
        
        data = {} ; i=0
        for t in tip :
            data[i]={'tip'       : t.tip}

            i= i+1

        print(data)

        return Response(data)


from django.db.models import Q

@api_view(['GET'])
def ill_treat_search_view(request, ch ): # search ills start with {ch} 

     if request.method == 'GET':
        
        illnesse = Illnesse.objects.all().filter( Q(ill_name__startswith=ch.lower())|  Q(ill_name__startswith=ch.upper()))
        
        data = {} ; lis = [] ; i=0
        for l in illnesse :
            lis=[]
            data[i]={
                  'ill_name'       : l.ill_name 
                #   'treats'     : [lis.append(t.treat_name) for t in l.treat.all()]
                  } 
            for t in l.treat.all():
                lis.append(t.treat_name)

            data[i]['treats']= lis

            i= i+1

        print(data)

        return Response(data)


@api_view(['GET'])
def try_view(request):

     if request.method == 'GET': 
        
        illnesse = Illnesse.objects.all()
        
        data = {} ; lis = [] ; i=0
        for l in illnesse :
            dic= {}
            data[i]={
                #   'song_name'       : l.ill_name , 
                #   'treat'     : for t in l.treat
                  } 
            i= i+1

        d= [ i for i in rang(5)]
        print (d)

        return Response({})


from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from PIL import Image
from account.serializers import PicSerializer,Pic

class Album_View(APIView):
    parser_classes = (FileUploadParser,)

    def get (self ,request , pk ):
        baby = Account.objects.get(id=pk)
        albums = Album.objects.all().filter(baby = baby)   
        lis = []; i = 0
        for f in albums:
            obj = Pic( f.image )

            serializer = PicSerializer(obj)
            lis.append(serializer.data['image'])
            i=+1
        
        return Response({"data": lis})

    def post(self ,request , pk ):
        file = request.data['file']
        user =Account.objects.get(id=pk)

        if file:
            user.image = file
            user.save()
            img = Image.open(file)
            return Response({"mode": img.mode, "size": img.size, "format": img.format})
        else : 
            return Response({'massege':'error'} , status=400)
