from core.models import BaseModel, BaseModelWithSlug
from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail

from .validators import validate_must_be_param


class Item(BaseModel):
    name = models.CharField(
        'название',
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
    )

    class Meta:
        default_related_name = 'items'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.text[:15]


class OneImage(models.Model):
    upload = models.ImageField(
        'Фото',
        upload_to='uploads./%Y/%m',
        default=''
    )

    class Meta:
        default_related_name = 'photo'
        verbose_name = 'фото'
        verbose_name_plural = 'фото'

    @property
    def get_img(self):
        return get_thumbnail(
            self.upload,
            '300x300',
            crop='center',
            quality=51
        )

    def image_tmb(self):
        if self.upload:
            return mark_safe(
                f'<img src="{self.get_img.url}"'
            )
        return "Нет изображения"

    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True


class Gallery(models.Model):
    upload = models.ImageField(
        'Галерея',
        upload_to='uploads./%Y/%m',
        default=''
    )

    class Meta:
        default_related_name = 'gallery'
        verbose_name = 'галерея'
        verbose_name_plural = 'галерея'

    @property
    def get_img(self):
        return get_thumbnail(
            self.upload,
            '300x300',
            crop='center',
            quality=51
        )

    def image_tmb(self):
        if self.upload:
            return mark_safe(
                f'<img src="{self.get_img.url}"'
            )
        return "Нет галереи"

    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True

    item = models.ForeignKey(
        Item,
        related_name="",
        verbose_name='галерея',
        help_text='Выберите галерею',
        on_delete=models.CASCADE
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

    def __str__(self):
        return self.text[:15]


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

    def __str__(self):
        return self.text[:15]
