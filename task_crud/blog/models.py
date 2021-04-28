from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title

class Reader(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64, )
    user_name = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)