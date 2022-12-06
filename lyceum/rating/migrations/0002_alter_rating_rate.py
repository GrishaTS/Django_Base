# Generated by Django 3.2.16 on 2022-12-06 14:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rate',
            field=models.IntegerField(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Ok'), (4, 'Good'), (5, 'Very Good')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]