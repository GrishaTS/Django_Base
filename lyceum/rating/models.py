from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import UniqueConstraint

from catalog.models import Item


class Rating(models.Model):
    class Rate(models.IntegerChoices):
        Ненависть = 1
        Неприязнь = 2
        Нейтрально = 3
        Обожание = 4
        Любовь = 5
        __empty__ = 'Без оценки'

    rate = models.IntegerField(
        'оценка',
        choices=Rate.choices,
    )
    item = models.ForeignKey(
        Item,
        verbose_name='товар',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='пользователь',
        on_delete=models.CASCADE,
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=('user', 'item'),
                name='rating_unique',
            )
        ]
