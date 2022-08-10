from django.contrib import admin
from app.models import *

class Feed_admin(admin.ModelAdmin):

     list_display=( 'food_name',
                    'food_type',
                    # 'food_icon',
                    'age_related',)

admin.site.register(Feed,Feed_admin)




class Feed_admin(admin.ModelAdmin):

     list_display=( 'sleep_duration',
                    'age_related',   )

admin.site.register(Sleep , Feed_admin)




class Lalluby_admin(admin.ModelAdmin):

     list_display=( 'song_name',
                    'file',   )

admin.site.register(Lalluby , Lalluby_admin)




class Treatment_admin(admin.ModelAdmin):

     list_display=( 'treat_name', )

admin.site.register(Treatment , Treatment_admin)




class Tips_admin(admin.ModelAdmin):

     list_display=( 'title',
                    'tip',
                    'age_related', )

admin.site.register(Tips , Tips_admin)




class Album_admin(admin.ModelAdmin):

        def treat_name(self,obj):
            return obj.baby.id
 
        list_display=( 'baby_id',
                       'image', )

admin.site.register(Album , Album_admin)

 


class Illnesse_admin(admin.ModelAdmin):

        list_display = ['ill_name', 'treat_name']
        list_display_links = ['treat_name']
         
        def treat_name(self,obj):

            return [t.treat_name for t in obj.treat.all()]
        
admin.site.register(Illnesse,Illnesse_admin)
