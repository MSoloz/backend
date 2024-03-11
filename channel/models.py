from django.db import models

class Channel(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.CharField(max_length=255)
    icon_path = models.ImageField(upload_to='images/')
    user = models.ForeignKey(to ='user.CustomUser', on_delete=models.CASCADE)
   
    def __str__(self):
        return self.title 
    
    class Meta:
        db_table = 'channels'
