from django.db import models


class Rating(models.Model):

    value = models.IntegerField()
    capsule = models.ForeignKey(to ='capsule.Capsule', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'ratings'
