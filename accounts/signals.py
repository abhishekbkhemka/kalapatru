from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.conf import settings

from .models import UserProfile


@receiver(post_save, sender=User)
def ensure_user_profile(sender, instance, created, **kwargs):
    if created:
        role = settings.ROLE_ADMIN if instance.is_superuser else settings.ROLE_VIEWER
        UserProfile.objects.create(user=instance, role=role)
    else:
        UserProfile.objects.get_or_create(
            user=instance,
            defaults={
                'role': settings.ROLE_ADMIN if instance.is_superuser else settings.ROLE_VIEWER,
            },
        )
