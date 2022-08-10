from django.contrib import admin
from account.models import Account#,Profile
# Register your models here.



class Account_admin(admin.ModelAdmin):
    
     list_display=(
            'id',
            'babyname',
            'email',
            'password',
            'father',
            'mother',
            'address',
            'birth',
            'age_in_days',
            'pragnancyduration',
            'gender',
            'cm_length',
            'kg_weight',
            'arrangement_among_siblings',
            'image',
     )


admin.site.register( Account, Account_admin )