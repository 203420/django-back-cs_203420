from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    id_user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    url_image = models.ImageField(blank='',default='',upload_to='img/')