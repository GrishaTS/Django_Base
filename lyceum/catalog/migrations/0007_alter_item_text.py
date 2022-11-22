# Generated by Django 3.2.16 on 2022-11-22 19:42

import catalog.validators
import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_item_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=ckeditor.fields.RichTextField(help_text='В тексте должны быть слова "превосходно" или "роскошно"', validators=[catalog.validators.validate_must_be_param], verbose_name='описание'),
        ),
    ]
