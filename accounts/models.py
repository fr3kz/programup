from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='images/accounts/')
    projects = models.ForeignKey(Project,on_delete=models.CASCADE,blank=True, null=True)
    user_points = models.IntegerField(default=0)
    name = models.CharField(max_length=25)
    github = models.CharField(max_length=25,blank=True, null=True)
    def __str__(self):
        return "ddd"


        