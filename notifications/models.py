from django.db import models


class Notification(models.Model):

    text = models.CharField(max_length=255)
    user = models.ForeignKey(to ='user.CustomUser', on_delete=models.CASCADE)
    capsule = models.ForeignKey(to ='capsule.Capsule', on_delete=models.CASCADE)
    channel = models.ForeignKey(to ='channel.Channel', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'notifications'
