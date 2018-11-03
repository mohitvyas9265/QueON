from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Name = models.CharField(max_length=100, default='')
    Branch = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default=0)

def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profiles = UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)
# Create your models here.
