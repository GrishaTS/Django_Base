from core.models import BaseModelName
from django.db import models


class Feedback(BaseModelName):
    email = models.EmailField(
        'Почта',
        max_length=320,
        help_text='Максимум 320 символов',
        null=True,
    )
    text = models.TextField(
        'Текст'
    )
    created_on = models.DateTimeField(auto_now_add=True, null=True)
