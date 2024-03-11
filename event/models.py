from django.db import models


class Event(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    image_path = models.ImageField(upload_to='images/')
    video_path = models.FileField(upload_to='videos/',blank=True)
    channel = models.ForeignKey(to ='channel.Channel', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    interested = models.ManyToManyField(to='user.CustomUser', related_name='interested_events',blank=True)
    participated = models.ManyToManyField(to='user.CustomUser', related_name='participated_events',blank=True)
    sponsors = models.ManyToManyField(to='sponsor.Sponsor', related_name='event_sponsors',blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
  
    class Meta:
        db_table = 'events'
