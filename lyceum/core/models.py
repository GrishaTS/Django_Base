from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail


class BaseModel(models.Model):
    is_published = models.BooleanField(
        'опубликовано',
        default=True,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class BaseModelWithSlug(BaseModel):
    slug = models.SlugField(
        'слаг',
        help_text='Максимальная длина 200',
        max_length=200,
    )

    class Meta:
        abstract = True


class BaseModelImage(models.Model):
    upload = models.ImageField(
        'Фото',
        upload_to='uploads/%Y/%m',
        default=''
    )

    name = models.CharField(
        'название',
        unique=True,
        help_text='Максимальная длина 150',
        max_length=150,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    @property
    def get_img(self):
        return get_thumbnail(
            self.upload,
            '300x300',
            crop='center',
            quality=51
        )

    def image_tmb(self):
        print(self.upload)
        if self.upload:
            return mark_safe(
                f'<img src="{self.get_img.url}"'
            )
        return "Нет изображения"

    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)
