from ckeditor.fields import RichTextField
from django.db import models

from catalog.validators import ValidateMustBeParam
from core.models import BaseModel, BaseModelImage, BaseModelWithSlug


class ItemManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset()
            .select_related('category')
            .prefetch_related(
                models.Prefetch(
                    'tags',
                    queryset=Tag.objects.published(),
                )
            )
            .select_related('photo')
        )

    def published(self):
        return (
            self.get_queryset()
            .filter(is_published=True)
            .order_by('name')
            .only('id', 'name', 'text', 'category__name', 'tags', 'photo',)
        )


class Item(BaseModel):
    objects = ItemManager()

    is_on_main = models.BooleanField(
        'на главную',
        default=False,
    )
    name = models.CharField(
        'название',
        unique=True,
        help_text='Максимальная длина 150',
        max_length=150,
    )
    text = RichTextField(
        'описание',
        validators=[ValidateMustBeParam('роскошно', 'превосходно')],
        help_text='В тексте должны быть слова "превосходно" или "роскошно"',
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

    class Meta:
        default_manager_name = 'objects'
        default_related_name = 'items'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class MainImage(BaseModelImage):
    item = models.OneToOneField(
        'Item',
        verbose_name='главное изображение',
        help_text='Выберите изображение',
        on_delete=models.CASCADE,
        null=True
    )

    class Meta:
        default_related_name = 'photo'
        verbose_name = 'фото'
        verbose_name_plural = 'фото'


class GalleryImage(BaseModelImage):
    item = models.ForeignKey(
        Item,
        related_name='item',
        verbose_name='товар',
        help_text='Выберите товар',
        on_delete=models.CASCADE,
    )

    class Meta:
        default_related_name = 'gallery'
        verbose_name = 'фото'
        verbose_name_plural = 'фотогалерея'


class TagManager(models.Manager):
    def published(self):
        return (
            self.get_queryset()
            .filter(is_published=True)
            .only('name')
        )


class Tag(BaseModelWithSlug):
    objects = TagManager()

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
