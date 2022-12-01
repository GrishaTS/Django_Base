# Generated by Django 3.2.16 on 2022-12-01 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True, verbose_name='почта'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_active',
            field=models.BooleanField(default=True, null=True, verbose_name='активная учетная запись'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_staff',
            field=models.BooleanField(default=True, null=True, verbose_name='сотрудник'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_superuser',
            field=models.BooleanField(default=False, null=True, verbose_name='Админ'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='фамилия'),
        ),
    ]
