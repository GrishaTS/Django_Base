from datetime import datetime

from django.contrib.auth.base_user import BaseUserManager


class ProfileManager(BaseUserManager):
    def is_activated(self):
        return (self.get_queryset().filter(is_active=True))

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if not extra_fields.get('is_staff'):
            raise ValueError('Superusers must have is_staff=True')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superusers must have is_superuser=True')
        return self.create_user(email, password, **extra_fields)

    def published(self):
        return (
            self.get_queryset()
            .filter(birthday=datetime.today())
            .values('email', 'first_name')
        )
