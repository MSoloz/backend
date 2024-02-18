from django.db import models


class Event(models.Model):

    text = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image_path = models.ImageField(upload_to='images/')
    video_path = models.FileField(upload_to='videos/')
    channel = models.ForeignKey(to ='channel.Channel', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    interested = models.ManyToManyField(to='user.CustomUser', related_name='interested_events')
    participated = models.ManyToManyField(to='user.CustomUser', related_name='participated_events')
    sponsors = models.ManyToManyField(to='sponsor.Sponsor', related_name='event_sponsors')
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
  
    class Meta:
        db_table = 'events'
