# Generated by Django 3.2.16 on 2022-12-05 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'default_related_name': 'fback', 'verbose_name': 'заявку на фидбек', 'verbose_name_plural': 'заявки на фидбек'},
        ),
    ]
