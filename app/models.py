from django.db import models

from account.models import *  
from vaccine.models import *  
from django.db.models.signals import pre_save, post_save
from PIL import Image

TYPES = (
    ('Breast milk','Breast milk'),
    ('Formula milk','Formula milk'),
	('Water','Water'),
	('Fruits','Fruits'),
	('Vegetables','Vegetables'),
	('Cyrbohedats','Cyrbohedats'),
	('Cremy','Cremy'),
)

class Feed(models.Model):
    food_name = models.CharField(max_length=300, null=True , default='default food', verbose_name='food details') 
    food_type = models.CharField(max_length=25,choices=TYPES, null=True , default='default type')
    food_icon = models.ImageField(default=None, null=True, blank=True)

    age_related = models.CharField(default= 1,max_length=10,verbose_name = "age related (in months)") # age related in months

# def Feed_post_save(sender, instance, created, **kwargs):
# 	if created and instance.food_icon != None :
#             image = Image.open(instance.food_icon)
#             image = image.resize((50,50))
#             instance.food_icon = image
#             print(instance.food_icon)


# post_save.connect(Feed_post_save, sender=Feed)
def upload_album_location(instance, filename, **kwargs):
	file_path = '/'.join(['images', str(instance.baby.id),'album', filename]) 
    
	return file_path



class Sleep(models.Model):
    sleep_duration = models.CharField(max_length=8 , default = '15', blank=True , null=True, verbose_name= 'sleep duration (in hours)' ) #sleep_duration in hours
    age_related = models.IntegerField(default= 1, verbose_name= 'age related (in months)' ) # age related in months
    
import os
class Lalluby(models.Model):
    song_name = models.CharField(max_length=100 , default = 'default song', blank=True , null=True )
    file = models.FileField(upload_to='audio',default=None, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.song_name = os.path.basename(self.file.name)
        super(Lalluby, self).save(*args, **kwargs)


class Treatment(models.Model):
    treat_name = models.CharField(max_length= 300 , default = 'default treat' , null=True)
    def __str__(self):
        return self.treat_name


class Illnesse(models.Model):
    ill_name = models.CharField(max_length= 50 , default = 'default ill' , null=True)
    treat = models.ManyToManyField(Treatment)

    def __str__(self):
        return self.ill_name


class Tips(models.Model):
    title =       models.TextField(max_length=2000, default = 'default title', null=True, blank=True)
    tip =         models.TextField(max_length=2000, default = 'default tip', null=True, blank=True)
    age_related = models.CharField(max_length= 10 , default = '1' , null=False) # age related in months


class Album(models.Model):
    baby                = models.ForeignKey(Account, on_delete=models.CASCADE, null=True , blank=True) 
    image = models.FileField(default=None, null=True, blank=True,upload_to=upload_album_location)

