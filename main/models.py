from django.db import models


# Create your models here.
class Url(models.Model):
    original_url = models.TextField()
    hash = models.CharField(max_length=10)
    creation_date = models.DateTimeField('creation date',auto_now_add=True)


class View(models.Model):

    url = models.ForeignKey(Url,on_delete=models.CASCADE,related_name='views')
    ip_adress = models.CharField(max_length=255)
    user_device = models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
