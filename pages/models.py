from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class movie_infos(models.Model):
    title = models.TextField()
    movieıd = models.IntegerField()
    path = models.URLField()
    user = models.ForeignKey(User,on_delete=models.SET_NULL,blank = True,null=True,)


    def __str__(self):
        return self.title

class deneme(models.Model):
    deneme = models.JSONField()