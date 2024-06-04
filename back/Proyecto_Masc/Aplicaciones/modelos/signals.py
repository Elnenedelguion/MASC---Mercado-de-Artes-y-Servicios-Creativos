from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserToken

User = get_user_model()

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        refresh = RefreshToken.for_user(instance)
        print(f'Refresh token: {refresh}')
        access_token = str(refresh.access_token)
        print(f'Access token: {access_token}')
        UserToken.objects.create(user=instance, token=access_token)
        print(f'Token stored in database for user {instance.username}')