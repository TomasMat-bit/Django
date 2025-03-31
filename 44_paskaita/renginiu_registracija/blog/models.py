from django.db import models
from django.contrib.auth.models import User


class Theme(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    themes = models.ManyToManyField('Theme', related_name='events')
    organizer = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Registration(models.Model):
    comment = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')

    def __str__(self):
        return f'Registration for {self.event.title}'

class Profile(models.Model):
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

   # def __str__(self):
   #     return f'Profile for {self.user.username}'

