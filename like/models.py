from django.db import models


class Like(models.Model):

    user = models.ForeignKey(to ='user.CustomUser', on_delete=models.CASCADE)
    capsule = models.ForeignKey(to ='capsule.Capsule', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'likes'
