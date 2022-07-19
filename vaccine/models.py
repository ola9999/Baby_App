from django.db import models
from django.conf import settings
from datetime import datetime, timedelta
from account.models import Account
from django.db.models.signals import pre_save, post_save

from functools import partial


def calc_date(self):
    return self.baby.birth + timedelta(days = self.vaccine.static_duration*30)

################
class All_Vaccines(models.Model):
    vacine_name 				= models.CharField(verbose_name="name", max_length=60)
    dose_num            = models.PositiveSmallIntegerField(default=1)
    static_duration     = models.PositiveSmallIntegerField(default=1 , verbose_name = "static duration in monthes")#age start with 0 means the first month


class B_V(models.Model):
    baby                = models.ForeignKey(Account, on_delete=models.CASCADE)
    vaccine             = models.ForeignKey(All_Vaccines, on_delete=models.CASCADE  )

    taken               = models.BooleanField(default=False)
    dead_line			= models.DateField(default=None,null=True ,verbose_name="date to take", editable=False)

    def save(self, *args, **kwargs):
        self.dead_line = calc_date(self)
        super(B_V, self).save(*args, **kwargs)
