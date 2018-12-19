from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PLanguage(models.Model):
    name = models.CharField(max_length=20) 
    def __str__(self):
        return self.name      

class Project(models.Model):
    thumbnail = models.ImageField(upload_to='images/projects')
    users = models.ManyToManyField(User)
    description = models.CharField(max_length=255)
    is_finished = models.BooleanField(default=False)
    author = models.CharField(max_length=20)
    github = models.CharField(max_length=20)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0) 
    is_pinned = models.BooleanField(default=False)
    title = models.CharField(max_length=20)
    language = models.ForeignKey(PLanguage,on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.title
