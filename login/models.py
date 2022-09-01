import datetime
from ctypes import util
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib import admin

class main_user(models.Model):
    fname_main = models.CharField(max_length=100)
    lname_main = models.CharField(max_length=100)
    email_main = models.CharField(max_length=100)
    phone_main = models.CharField(max_length=100)
    bday_main = models.DateTimeField('bday of main user')
    country_main = models.CharField(max_length=100)
    gender_main = models.CharField(max_length=100)
    user_main = models.CharField(max_length=100)
    pass_main = models.CharField(max_length=100)
    edit_main = models.DateTimeField('date edited')
    create_main = models.DateTimeField('date created')

    def __str__(self):
        return self.user_main

    def was_created_recently(self):
        return self.create_main >= timezone.now() - datetime.timedelta(days=1)