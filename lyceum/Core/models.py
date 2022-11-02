from django.db import models


class BaseModel(models.Model):
    name = models.CharField(
        "Название", help_text="Максимальная длина 150", max_length=150
    )
    is_published = models.BooleanField("Опубликовано", default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class BaseModelWithSlug(BaseModel):
    slug = models.SlugField(
        "Слаг",
        help_text="Максимальная длина 200",
        max_length=200
    )

    class Meta:
        abstract = True
