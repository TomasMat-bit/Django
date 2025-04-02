from django.db import models
from  django.contrib.auth.models import User
from django.template.context_processors import media


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profiliai/', blank=True, null=True)

    def __str__(self):
        return self.user.username

