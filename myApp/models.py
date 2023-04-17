from django.db import models
from django.contrib.auth import get_user_model
import datetime
import uuid


User=get_user_model()

# Create your models here.

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profileimg=models.ImageField(upload_to='profile_images',default="profile_images/default-user.png")
    firstsetting=models.BooleanField(default=False)
    profession=models.CharField(max_length=100,blank=True)
    id=models.AutoField(primary_key=True)
    bio=models.TextField(max_length=500,blank=True)
    linkedin=models.URLField(max_length=200,blank=True)
    github=models.URLField(max_length=200,blank=True)
    website=models.URLField(max_length=200,blank=True)
    twitter=models.URLField(max_length=200,blank=True)
    acadmicyear=models.CharField(max_length=200, blank=False,null=True)
    branch=models.CharField(max_length=30,blank=True)
    location=models.CharField(max_length=100,blank=True)
    mobilenumber=models.CharField(max_length=10,blank=True)
    view_count=models.IntegerField(default=0)
    # total_views = models.IntegerField(default=0)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username  #type:ignore
 
class Post(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    short_description = models.TextField(default="Short Description")
    long_description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    date_started = models.DateField(default=datetime.date.today)
    github_link = models.URLField(max_length=200, blank=True)
    website_link = models.URLField(max_length=200, blank=True)
    youtube_link = models.URLField(max_length=200, blank=True)
    custom_link = models.URLField(max_length=200, blank=True)
    image_1 = models.ImageField(upload_to='project_images', blank=True)
    image_2 = models.ImageField(upload_to='project_images', blank=True)
    image_3 = models.ImageField(upload_to='project_images', blank=True)
    post_thumbnail = models.ImageField(upload_to='project_images', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title