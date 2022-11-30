# from django.contrib.auth.models import User
# from django.db import models


# class ProfileManager(models.Manager):
#     def activated(self):
#         return (
#             self.get_queryset()
#             .select_related('user')
#             .filter(user__is_active=True)
#             .only(
#                'id',
#                'user__username',
#                'user__email',
#                'user__is_superuser'
#               )
#         )


# class Profile(models.Model):
#     objects = ProfileManager()

#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE
#     )
#     birthday = models.DateField(
#         'дата рождения',
#         blank=False,
#         null=True,
#         auto_now=False,
#         auto_now_add=False,
#     )

#     class Meta:
#         verbose_name = 'доп информация'
#         verbose_name_plural = 'доп информация'

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
    )
    last_name = models.CharField(
        'фамилия',
        max_length=150,
        blank=True,
    )
    email = models.EmailField(
        'почта',
        unique=True,
    )
    is_active = models.BooleanField(
        'активный пользователь',
        default=True,
    )
    is_staff = models.BooleanField(
        'сотрудник',
        default=True,
    )
    is_superuser = models.BooleanField(
        'Админ',
        default=False,
    )
    date_joined = models.DateTimeField(default=timezone.now)
    birthday = models.DateField(
        'день рождения',
        blank=True,
        null=True,
    )
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    class Meta:
        default_related_name = 'profiles'
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
