from django.contrib.auth.models import AbstractUser
from django.db import models

from project.settings import MEDIA_URL, STATIC_URL


# Create your models here.

class User(AbstractUser):
    CHOICE_ROL=[
        ('S','Supervisor de Calidad'),
        ('D','Desarrollador'),
        ('I','Diseñador'),
        ('A','Analista'),
    ]
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True,default='avatar/avatar.svg')
    #CHOICE_ROL | S= Supervisor de Calidad, D= Desarrollador , I= Diseñador , A= Analista
    rol=models.CharField(max_length=1, choices=CHOICE_ROL, default='D')
    def get_avatar(self):
        if self.avatar:
            return '{}{}'.format(MEDIA_URL, self.avatar)
        return '{}{}'.format(STATIC_URL, 'avatar/avatar.svg')

