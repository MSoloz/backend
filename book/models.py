from django.db import models

class Book(models.Model):

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    isFound = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    class Meta: 
       db_table = 'books'
