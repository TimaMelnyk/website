#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
# from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=15)
    def __unicode__(self):
        return self.user.username

class Order(models.Model):
    order_text = models.CharField(max_length=200,blank=False)
    prof = models.ForeignKey(UserProfile)
    def __str__(self):
        return self.order_text
    # def was_published_recently(self):
    #     return self.pub_date>=timezone.now() - datetime.timedelta(days=1)