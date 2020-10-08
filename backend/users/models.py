from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin) :
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20, unique=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_name'
    objects = CustomUserManager()


# class CustomUserProfile(models.Model):
#     user = models.OneToOneField(CustomUser, primary_key=True, on_delete=models.CASCADE, related_name='user')

#     def __str__(self):
#         return self.user.username

#     class Meta :
#         verbose_name = "Profile"
#         verbose_name_plural = "Profiles"