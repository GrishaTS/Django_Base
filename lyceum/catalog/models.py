from ckeditor.fields import RichTextField
from core.models import BaseModel, BaseModelImage, BaseModelWithSlug
from django.db import models

from .validators import validate_must_be_param


class ItemManager(models.Manager):
    def published(self):
        return (
            self.get_queryset()
            .filter(is_on_main=True)
            .select_related('category')
            .order_by('name')
            .prefetch_related(
                models.Prefetch(
                    'tags',
                    queryset=Tag.objects.published(),
                )
            )
            .prefetch_related(
                models.Prefetch(
                    'photo',
                    queryset=MainImage.objects.published(),
                )
            )
            .only('id', 'name', 'text', 'category__name', 'tags', 'photo')
        )

    def item_list(self):
        return (
            self.get_queryset()
            .filter(is_published=True)
            .select_related('category')
            .order_by('category__name')
            .prefetch_related(
                models.Prefetch(
                    'tags',
                    queryset=Tag.objects.published(),
                )
            )
            .prefetch_related(
                models.Prefetch(
                    'photo',
                    queryset=MainImage.objects.published(),
                )
            )
            .only('id', 'name', 'text', 'category__name', 'tags', 'photo')
        )


class Item(BaseModel):
    objects = ItemManager()

    is_on_main = models.BooleanField(
        'На главную',
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
        validators=[validate_must_be_param('превосходно', 'роскошно')],
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
        default_related_name = 'items'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class MainImageManager(models.Manager):
    def published(self):
        return (
            self.get_queryset()
        )


class MainImage(BaseModelImage):
    objects = MainImageManager()

    preview = models.OneToOneField(
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
        verbose_name='Товар',
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
