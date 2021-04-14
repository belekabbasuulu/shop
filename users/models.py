from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(
        max_length=255, blank=True, verbose_name="Имя")
    last_name = models.CharField(
        max_length=255, blank=True, verbose_name="Фамилия")
    username = models.CharField(
        max_length=255, unique=True, verbose_name="Имя пользователя")
    email = models.EmailField(
        max_length=254, verbose_name="email почта", blank=True)
    phone_number = models.CharField(
        max_length=255, blank=True, verbose_name="Номер телефона")
    address = models.CharField(
        max_length=255, blank=True, verbose_name="Адрес")
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.username
