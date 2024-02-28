from django.db import models


class Sponsor(models.Model):

    icon_path = models.ImageField(upload_to='images/')
    sponsor_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    website = models.CharField(max_length=255,blank=True)
    facebook = models.CharField(max_length=255,blank=True)
    twitter = models.CharField(max_length=255,blank=True)
    linkedin = models.CharField(max_length=255,blank=True)
    instagram = models.CharField(max_length=255,blank=True)
    vimo = models.CharField(max_length=255,blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'sponsors'
