from django.db import models


class Sponsor(models.Model):

    icon_path = models.ImageField(upload_to='images/')
    sponsor_name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    vimo = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'sponsors'
