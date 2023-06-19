from typing import Type
from django.db import models
from django.db.models.options import Options

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    brief_description = models.CharField(max_length=50)
    description = models.TextField()
    technology = models.CharField(max_length=75)
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title 
    
    
    