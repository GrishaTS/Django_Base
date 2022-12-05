# Generated by Django 3.2.16 on 2022-12-05 12:02

import catalog.validators
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_item_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='is_on_main',
            field=models.BooleanField(default=False, verbose_name='на главную'),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=ckeditor.fields.RichTextField(help_text='В тексте должны быть слова "превосходно" или "роскошно"', validators=[catalog.validators.validate_must_be_param], verbose_name='описание'),
        ),
    ]