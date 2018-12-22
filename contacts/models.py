from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    message = models.TextField()