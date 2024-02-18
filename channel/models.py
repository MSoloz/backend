from django.db import models

class Channel(models.Model):

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    icon_path = models.ImageField(upload_to='images/')
   
    def __str__(self):
        return self.title 
    
    class Meta:
        db_table = 'channels'
