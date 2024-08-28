from django.db import models

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