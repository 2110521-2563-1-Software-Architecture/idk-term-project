from django.db import models
from users.models import CustomUser
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Link(models.Model) :
    link_shorten = models.CharField(max_length=5, validators=[MinLengthValidator(5)], primary_key=True)
    link_original = models.CharField(max_length = 200)
    link_user = models.ForeignKey(CustomUser, related_name='links_user', on_delete=models.CASCADE)

    def __str__(self) :
        return 'idk.ly/' + self.link_shorten + '\n' + self.link_original + '\n[BY:' + self.link_user.user_name + ']'