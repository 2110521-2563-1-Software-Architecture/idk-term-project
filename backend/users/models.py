from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class CustomUser(AbstractUser) :
    user_id = models.AutoField(primary_key=True)

    REQUIRED_FIELDS = []
    objects = CustomUserManager()


class CustomUserProfile(models.Model):
    user = models.OneToOneField(CustomUser, primary_key=True, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return self.user.username

    class Meta :
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"