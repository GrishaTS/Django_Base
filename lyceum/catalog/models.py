from Core.models import BaseModel, BaseModelWithSlug
from django.db import models

from .validators import validate_must_be_param


class Item(BaseModel):
    text = models.TextField(
        "Текст",
        help_text='В текста должно быть слово превосходно или роскошно',
        validators=[validate_must_be_param('превосходно', 'роскошно')]
    )
    category = models.ForeignKey(
        'Category',
        verbose_name='Категория',
        help_text='Выберите категории',
        on_delete=models.CASCADE,
    )
    tags = models.ManyToManyField(
        'Tag',
        verbose_name='Тег',
        help_text='Выберите тег',
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Tag(BaseModelWithSlug):
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Category(BaseModelWithSlug):
    weight = models.SmallIntegerField(
        'Вес',
        help_text='от 0 до 32767, значение по умолчанию 100',
        default=100
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
