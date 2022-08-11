from django.db import models
from datetime import  timedelta,date
from django.db.models.signals import pre_save, post_save


def upload_profile_image_location(instance, filename, **kwargs):
	file_path = '/'.join(['images', str(instance.id),'profile image', filename]) 
    
	return file_path


BABY_GENDER = (
    ('Male','Male'),
    ('Female','Female'),
)

class Account(models.Model):

	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True, default= "a@a.com")
	password				= models.CharField(max_length=30 , default="default")

	babyname 				= models.CharField(max_length=40 , default="default")
	father					= models.CharField(max_length=40 , default="default")
	mother					= models.CharField(max_length=40 , default="default")
	address					= models.CharField(max_length=250, default="default")

	birth					= models.DateField(auto_now=False,default= date.today(),null=True, verbose_name="birth" )
	age_in_days				= models.IntegerField(verbose_name="age in days", null=True,blank=True , default=None)#age in days

	pragnancyduration		= models.CharField(max_length=2 , default="9")
	gender					= models.CharField(max_length=10 ,choices=BABY_GENDER , default="default")

	cm_length				= models.CharField(max_length=10 , default="default")
	kg_weight				= models.CharField(max_length=10 , default="default")

	arrangement_among_siblings = models.CharField(max_length=10 , default="default")
	image 					= models.FileField(default=None, null=True, blank=True, upload_to=upload_profile_image_location)
	# profile_image 			= models.ImageField(max_Length= 255 , upload_to= get_profile_image_filepath , null = True ,blank= True, default =get_default_profile_image )
	def save(self, *args, **kwargs):
		self.age_in_days = (date.today() - self.birth).days 

		super(Account, self).save(*args, **kwargs)


def calc_date(bab,vac):
    return bab.birth + timedelta(days = vac.static_duration*30)



from vaccine.models import B_V,All_Vaccines



def vaccin_post_save(sender, instance, created, **kwargs):
	if created:

		vaccine = All_Vaccines.objects.all()
		vac_list = []

		for vac in vaccine:
			b_v= B_V(baby=instance, vaccine= vac, dead_line=calc_date(instance, vac) )
			vac_list.append(b_v)
		
		B_V.objects.bulk_create(vac_list)

post_save.connect(vaccin_post_save, sender=Account)

