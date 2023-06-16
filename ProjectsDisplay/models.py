from typing import Type
from django.db import models
from django.db.models.options import Options

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")

    def __str__(self):
        return self.title 
    
    