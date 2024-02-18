from django.db import models

class Rubric(models.Model):

    title = models.CharField(max_length=255)
    position = models.IntegerField()
    channel = models.ForeignKey(to ='channel.Channel', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'rubrics'
