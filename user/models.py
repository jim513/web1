from django.db import models
from django.contrib.auth.models import User
from post.models import Post
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    location = models.CharField(max_length=50,null=True,blank=True)
    url =models.CharField(max_length=80, null=True,blank=True)
    profile_info =models.TextField(max_length=80, null=True,blank=True)
    user_created = models.DateField(auto_now=False, auto_now_add=True)
    favorites = models.ManyToManyField(Post)
    objects=models.Manager()

    def __str__(self):
        return self.user