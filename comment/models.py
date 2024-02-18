from django.db import models


class Comment(models.Model):

    text = models.CharField(max_length=255)
    capsule = models.ForeignKey(to ='capsule.Capsule', on_delete=models.CASCADE)
    user = models.ForeignKey(to ='user.CustomUser', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'
