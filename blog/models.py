from django.utils import timezone
from django.db import models
from django.urls import reverse

# Create your models here.

#Base class for Entrys
class BaseEntryModel(models.Model):
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=30)
    rating = models.IntegerField(default = 5)
    #Tells Django to not create tables for this class
    class Meta:
        abstract = True
        ordering = ['pub_date']


class Post(BaseEntryModel):
    title = models.CharField(max_length=100, unique=True)
    body_text = models.TextField()
    mod_date = models.DateTimeField(auto_now = True)
    number_of_comments = models.IntegerField(default=0)

    #BaseEntryModel is passed and therefore Post's Meta class inherits BaseEntryModel's Meta class (excpet abstract setting)
    class Meta(BaseEntryModel.Meta):
        pass
    
    def __str__(self):
        return self.title
    
   #allows access to a specific post via the admin page 
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk' : self.pk})

    def update_comment_count(self):
        number_of_comments += 1

class Comment(BaseEntryModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    comment_text = models.CharField(max_length=300)

    class Meta(BaseEntryModel.Meta):
       pass

    def __str__(self):
       return self.comment_text 
