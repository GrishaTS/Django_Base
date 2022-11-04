from django.db import models


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
