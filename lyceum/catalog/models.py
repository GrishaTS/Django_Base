from core.models import BaseModel, BaseModelImage, BaseModelWithSlug
from django.db import models

from .validators import validate_must_be_param


class Item(BaseModel):
    name = models.CharField(
        'название',
        unique=True,
        help_text='Максимальная длина 150',
        max_length=150,
    )
    text = models.TextField(
        'Текст',
        help_text='В тексте должны быть слова "превосходно" или "роскошно"',
        validators=[validate_must_be_param('превосходно', 'роскошно')],
    )
    category = models.ForeignKey(
        'Category',
        verbose_name='категория',
        help_text='Выберите категории',
        on_delete=models.CASCADE,
    )
    tags = models.ManyToManyField(
        'Tag',
        verbose_name='тег',
        help_text='Выберите тег',
    )
    preview = models.OneToOneField(
        'OneImage',
        verbose_name='фотография',
        help_text='Выберите фотографию',
        on_delete=models.CASCADE,
        primary_key=True,
        default='',
    )

    class Meta:
        default_related_name = 'items'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class OneImage(BaseModelImage):

    class Meta:
        default_related_name = 'photo'
        verbose_name = 'фото'
        verbose_name_plural = 'фото'


class Gallery(BaseModelImage):

    class Meta:
        default_related_name = 'gallery'
        verbose_name = 'галерею'
        verbose_name_plural = 'галерея'

    item = models.ForeignKey(
        Item,
        related_name='item',
        verbose_name='Товар',
        help_text='Выберите товар',
        on_delete=models.CASCADE,
    )


class Tag(BaseModelWithSlug):
    name = models.CharField(
        'название',
        unique=True,
        help_text='Максимальная длина 150',
        max_length=150,
    )

    class Meta:
        default_related_name = 'tags'
        verbose_name = 'тег'
        verbose_name_plural = 'теги'


class Category(BaseModelWithSlug):
    name = models.CharField(
        'название',
        unique=True,
        help_text='Максимальная длина 150',
        max_length=150,
    )
    weight = models.SmallIntegerField(
        'вес',
        help_text='от 0 до 32767, значение по умолчанию 100',
        default=100,
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = 'weight', 'id'
