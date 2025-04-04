from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserLog

@receiver(post_save, sender=User)
def create_user_log(sender, instance, created, **kwargs):
    if created:  # Tik jei vartotojas buvo sukurtas
        UserLog.objects.create(
            user=instance,
            action="Vartotojas sukurtas"
        )

@receiver(post_delete, sender=User)
def create_user_delete_log(sender, instance, **kwargs):
    UserLog.objects.create(
        user=instance,
        action="Vartotojas ištrintas"
    )
