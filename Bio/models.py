from django.db import models

# Create your models here.
class Bio(models.Model):
    name = models.CharField(max_length=12)
    body = models.TextField()
    prof_pic = models.FileField(null=True, blank=True)
    linkedIn_link = models.URLField(default=None)
    github_link = models.URLField(default=None)
    