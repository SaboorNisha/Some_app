from django.db import models
from django.contrib.auth import get_user_model
from uuid import uuid4
from datetime import datetime

User=get_user_model()


# Create your models here.
class account_profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    id_user=models.IntegerField()
    bio=models.TextField(blank=True)
    profile_image=models.ImageField(upload_to='profile_image',default="blank-profile")
    location=models.CharField(max_length=100,blank=True)
    
    def __str__(self) -> str:
        return self.user.username
        
class Post(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid4)
    user=models.CharField(max_length=100)
    image=models.ImageField(upload_to='post_image')
    caption=models.TextField()
    created_at=models.DateTimeField(default=datetime.now)
    no_of_likes=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user
    
    