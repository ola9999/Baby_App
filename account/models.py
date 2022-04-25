from django.db import models
from datetime import  timedelta,date
from django.db.models.signals import pre_save, post_save


BABY_GENDER = (
    ('Male','Male'),
    ('Female','Female'),
	# ('female','female'),
	# ('male','male'),
)

class Account(models.Model):

	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	password				= models.CharField(max_length=30)

	babyname 				= models.CharField(max_length=40)
	father					= models.CharField(max_length=40)
	mother					= models.CharField(max_length=40)
	address					= models.CharField(max_length=250)

	birth					= models.DateField(auto_now=False,default= date.today(),null=True, verbose_name="birth" )

	pragnancyduration		= models.CharField(max_length=2)
	gender					= models.CharField(max_length=10 ,choices=BABY_GENDER)

	cm_length				= models.CharField(max_length=10)
	kg_weight				= models.CharField(max_length=10)

	arrangement_among_siblings = models.CharField(max_length=10)
	image 					= models.ImageField(default=None, null=True, blank=True)
	# profile_image 			= models.ImageField(max_Length= 255 , upload_to= get_profile_image_filepath , null = True ,blank= True, default =get_default_profile_image )

def calc_date(bab,vac):
    return bab.birth + timedelta(days = vac.static_duration*30)

from vaccine.models import B_V,All_Vaccines


def vaccin_post_save(sender, instance, created, **kwargs):
	if created:

		print('hello')
		vaccine = All_Vaccines.objects.all()
		vac_list = []

		for vac in vaccine:
			b_v= B_V(baby=instance, vaccine= vac, dead_line=calc_date(instance, vac) )
			vac_list.append(b_v)
		
		print('before balk')
		B_V.objects.bulk_create(vac_list)
		print('pre_save')


post_save.connect(vaccin_post_save, sender=Account)
