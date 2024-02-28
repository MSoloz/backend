from django.db import models


class Capsule(models.Model):

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image_path = models.ImageField(upload_to='images/')
    video_path = models.FileField(upload_to='videos/')
    channel = models.ForeignKey(to ='channel.Channel', on_delete=models.CASCADE)
    rubric = models.ForeignKey(to ='rubric.Rubric', on_delete=models.CASCADE)
    sponsors = models.ManyToManyField(to='sponsor.Sponsor', related_name='capsule_sponsors',blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'capsules'
