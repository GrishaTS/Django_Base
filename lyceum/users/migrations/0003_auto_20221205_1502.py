# Generated by Django 3.2.16 on 2022-12-05 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20221202_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_staff',
            field=models.BooleanField(default=False, null=True, verbose_name='сотрудник'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_superuser',
            field=models.BooleanField(default=False, null=True, verbose_name='админ'),
        ),
    ]
