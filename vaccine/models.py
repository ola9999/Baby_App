from django.db import models
from django.conf import settings
from datetime import datetime, timedelta
from account.models import Account
from django.db.models.signals import pre_save, post_save

from functools import partial


def calc_date(self):
    return self.baby.birth + timedelta(days = self.vaccine.static_duration*30)

# class CustomManager(models.Manager):
#     def get_queryset(self):
#         return super(CustomManager, self).get_queryset().defer('dead_line',)

class All_Vaccines(models.Model):
    # baby                = models.ForeignKey(Account, on_delete=models.CASCADE)
    vacine_name 				= models.CharField(verbose_name="name", max_length=60)
    dose_num            = models.PositiveSmallIntegerField(default=1)
    static_duration     = models.PositiveSmallIntegerField(default=1 , verbose_name = "static duration in monthes")


class B_V(models.Model):
    baby                = models.ForeignKey(Account, on_delete=models.CASCADE)
    vaccine             = models.ForeignKey(All_Vaccines, on_delete=models.CASCADE  )

    taken               = models.BooleanField(default=False)
    dead_line			= models.DateField(default=None,null=True ,verbose_name="date to take", editable=False)

    # @receiver(post_save, sender=Account)
    # def post_save_user_receiever(sender, instance, created, **kwargs):
    #     if created:
            



    # def save(self, *args, **kwargs):
        
    #     print(self.dead_line)
    #     super(B_V, self).save(*args, **kwargs)


            


# class Vaccine(models.Model):


    # name 				= models.CharField(verbose_name="name", max_length=60)
    # dose_num            = models.PositiveSmallIntegerField(default=1)

    # static_duration     = models.PositiveSmallIntegerField(default=1 , verbose_name = "static duration in monthes")

    # objects = CustomManager()

