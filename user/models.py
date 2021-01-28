from django.db import models
from django.contrib.auth.models import User
from post.models import Post

from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=50, null=True,blank=True)
    url =models.CharField(max_length=80, null=True,blank=True)
    profile_info =models.TextField(max_length=80, null=True,blank=True)
    created = models.DateField(auto_now=False, auto_now_add=True)
    favorites = models.ManyToManyField(Post, blank=True)
    objects=models.Manager()
    picture = models.ImageField(upload_to='profile_pictures',blank=True, null=True,verbose_name='Picture')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
    
def create_user_profile(sender, instance, created,  **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
def svae_user_profile(sender, instance,  **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile,sender=User)
post_save.connect(svae_user_profile,sender=User)