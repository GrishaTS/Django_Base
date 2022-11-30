# Generated by Django 3.2.16 on 2022-11-30 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Максимальная длина 150', max_length=150, null=True, verbose_name='имя')),
                ('email', models.EmailField(help_text='Максимум 320 символов', max_length=320, null=True, verbose_name='почта')),
                ('text', models.TextField(verbose_name='текст')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Заявку на фидбек',
                'verbose_name_plural': 'Заявки на фидбек',
                'default_related_name': 'fback',
            },
        ),
    ]
