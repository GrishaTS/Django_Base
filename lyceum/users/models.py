from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from .managers import ProfileManager


class Profile(AbstractBaseUser, PermissionsMixin):
    objects = ProfileManager()

    first_name = models.CharField(
        'имя',
        max_length=150,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        'фамилия',
        max_length=150,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        'почта',
        unique=True,
        null=True,
    )
    is_active = models.BooleanField(
        'активная учетная запись',
        default=True,
        null=True,
    )
    is_staff = models.BooleanField(
        'сотрудник',
        default=True,
        null=True,
    )
    is_superuser = models.BooleanField(
        'Админ',
        default=False,
        null=True,
    )
    date_joined = models.DateTimeField(default=timezone.now)
    birthday = models.DateField(
        'день рождения',
        blank=True,
        null=True,
    )
    USERNAME_FIELD = 'email'

    class Meta:
        default_related_name = 'profiles'
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email
