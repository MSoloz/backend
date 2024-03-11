from django.db import models


class Setting(models.Model):

    platform_type_is_mobile = models.BooleanField(default=False)
    platform_type_is_web = models.BooleanField(default=False)
    logo = models.ImageField(upload_to='images/')
    favicon = models.ImageField(upload_to='images/')
    logo_footer = models.ImageField(upload_to='images/')
    width_logo = models.IntegerField()
    brand_color = models.CharField(max_length=255,blank=True)
    bg_color = models.CharField(max_length=255,blank=True)
    container_color = models.CharField(max_length=255,blank=True)
    text_color = models.CharField(max_length=255,blank=True)
    hover_color = models.CharField(max_length=255,blank=True)
    background_login = models.ImageField(upload_to='images/')
    background_internal = models.ImageField(upload_to='images/')
    facebook = models.URLField(max_length=255,blank=True)
    twitter = models.URLField(max_length=255,blank=True)
    linkedin = models.URLField(max_length=255,blank=True)
    instagram = models.URLField(max_length=255,blank=True)
    vimo = models.URLField(max_length=255,blank=True)
    channel = models.ForeignKey(to ='channel.Channel', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'settings'
