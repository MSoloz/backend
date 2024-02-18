from django.db import models


class Setting(models.Model):

    platform_type = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    favicon = models.CharField(max_length=255)
    background_login = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    vimo = models.CharField(max_length=255)
    channel = models.ForeignKey(to ='channel.Channel', on_delete=models.CASCADE)
   
    def __str__(self):
        return self.platform_type
    
    class Meta:
        db_table = 'settings'
