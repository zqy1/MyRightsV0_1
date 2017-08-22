from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    nickname = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    cellphone = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to='users/%Y/%m/%d/%H/%M', blank=True)

    def __str__(self):
        return self.user.username