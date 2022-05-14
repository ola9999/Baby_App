from django.db import models

from account.models import *  
from vaccine.models import *  

class Feed(models.Model):
    food_name = models.CharField(max_length=25, null=True , default='default food') 
    food_type = models.CharField(max_length=25, null=True , default='default type')
    food_icon = models.ImageField(default=None, null=True, blank=True)

    age_related = models.IntegerField(default= 1) # age related in years

class Sleep(models.Model):
    sleep_duration = models.IntegerField(default=16) #sleep_duration in hours
    age_related = models.IntegerField(default= 1) # age related in years

class Lalluby(models.Model):
    file = models.FileField(default=None, null=True, blank=True)

    song_name = models.CharField(max_length=100 , default = 'default song', blank=True , null=True )


class Treatment(models.Model):
    treat_name = models.CharField(max_length= 50 , default = 'default treat' , null=True)
    def __str__(self):
        return self.treat_name


class Illnesse(models.Model):
    ill_name = models.CharField(max_length= 50 , default = 'default ill' , null=True)
    treat = models.ManyToManyField(Treatment)

    def __str__(self):
        return self.ill_name


class Tips(models.Model):
    tip = models.TextField(max_length=2000, default = 'default tip')


class Album(models.Model):
    image = models.fileField(default=None, null=True, blank=True)
