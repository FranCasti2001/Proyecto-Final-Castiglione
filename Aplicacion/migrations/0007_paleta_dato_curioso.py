# Generated by Django 4.2 on 2023-05-14 19:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0006_paleta_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='paleta',
            name='dato_curioso',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
