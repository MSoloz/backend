from django.db import models


class Condition(models.Model):

    title = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    required = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='pdfs/')
    channel = models.ForeignKey(to ='channel.Channel', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'conditions'

