from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import UniqueConstraint

from catalog.models import Item


class Rating(models.Model):
    rate = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'item'], name='rating_unique')
        ]
