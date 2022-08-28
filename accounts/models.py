from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Customeuser(AbstractUser):
    age=models.PositiveIntegerField(null=True , default=0,verbose_name=_('age'))
    is_author=models.BooleanField(default=False,verbose_name=_('is_author'))
    email=models.EmailField(max_length=254,unique=True,verbose_name=_('email'))
    first_name=models.CharField(max_length=200,default='firstname',verbose_name=_('firstname'))
    last_name=models.CharField(max_length=200,default='lastname',verbose_name=_('lastname'))
    avatar=models.FileField(null=True,blank=True,upload_to='user_avatar',verbose_name=_('avatar'))
    class Meta:
        verbose_name=_('Custome_User')