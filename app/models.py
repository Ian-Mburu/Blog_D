from django.db import models
from django.contrib.auth.hashers import make_password

from django.utils import timezone
from cloudinary.models import CloudinaryField


# User
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

# Subscriber
class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

# Blog post
class RecipeDescription(models.Model):
    image = CloudinaryField("image", null=True)
    recipeTitle = models.CharField(max_length=200)
    recipeDescription = models.TextField()
    postedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Set default to a specific user ID
    date_posted = models.DateTimeField(auto_now_add=True)
    last_posted = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_posted']


    def __str__(self):
        return self.title
    
    def published (cls):
        return cls.objects.filter(is_published=True)

class UserPosted(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name