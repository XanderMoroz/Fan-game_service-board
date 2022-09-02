from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(verbose_name='Номер телефона', max_length=20, unique=True, db_index=True)
    is_adm = models.BooleanField(verbose_name= 'админ', default=False)
    number = models.CharField(verbose_name='одноразовый код', max_length=10, blank=True)