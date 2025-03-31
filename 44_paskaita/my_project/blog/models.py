from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    categories = models.ManyToManyField(Category)
    content = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()


