# Generated by Django 3.2.16 on 2022-12-07 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rate',
            field=models.IntegerField(blank=True, choices=[(None, 'Без оценки'), (1, 'Ненависть'), (2, 'Неприязнь'), (3, 'Нейтрально'), (4, 'Обожание'), (5, 'Любовь')], verbose_name='оценка'),
        ),
    ]
