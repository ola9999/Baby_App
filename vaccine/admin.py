from django.contrib import admin
from vaccine.models import All_Vaccines,B_V

class Vaccine_admin(admin.ModelAdmin):

     def baby_name(self,obj):
          return obj.baby.babyname

     def baby_birth(self,obj):
          return obj.baby.birth
     
     def vaccine_name(self,obj):
          return obj.vaccine.vacine_name
     def dose_num(self,obj):
          return obj.vaccine.dose_num
     def static_duration(self,obj):
          return obj.vaccine.static_duration

     list_display=('baby_name',
                    'baby_birth',
                    'vaccine_name',
                    'dose_num',
                    'static_duration',
                    'taken',
                    'dead_line',)

admin.site.register(B_V,Vaccine_admin)

class All_Vaccine_admin(admin.ModelAdmin):

     list_display=(
                    'vacine_name',
                    'dose_num',
                    'static_duration',)

admin.site.register(All_Vaccines, All_Vaccine_admin)