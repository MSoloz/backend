from django.db import models


class Condition(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    conditions_url = models.URLField(blank=True)
    pdf = models.FileField(upload_to='pdfs/',blank=True)
    channel = models.ForeignKey(to ='channel.Channel', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'conditions'

