# Generated by Django 4.2 on 2023-05-13 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0004_rename_año_de_creacion_equipo_anio_de_creacion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apodo', models.CharField(max_length=30)),
                ('dt', models.CharField(max_length=30)),
                ('anio_de_creacion', models.IntegerField()),
            ],
        ),
    ]
