from django.db import models

class Banner(models.Model):

    image_path1 = models.ImageField(upload_to='images/')
    image_path2 = models.ImageField(upload_to='images/')
    image_path3= models.ImageField(upload_to='images/')
    rubric = models.ForeignKey(to ='rubric.Rubric', on_delete=models.CASCADE)
    channel = models.ForeignKey(to ='channel.Channel', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'banners'
