# Generated by Django 4.1.1 on 2022-11-29 05:25

from django.db import migrations, models
import django.db.models.deletion
import galeria.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(blank=True, max_length=256, null=True, verbose_name='Categorias')),
                ('descripcion', models.TextField(blank=True, max_length=256, null=True, verbose_name='Descripcion')),
                ('activo', models.BooleanField(blank=True, max_length=256, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='imagenes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidad', models.CharField(blank=True, max_length=256, null=True, verbose_name='Unidad')),
                ('titulo', models.CharField(blank=True, max_length=256, null=True, verbose_name='Titulo')),
                ('descripcion', models.TextField(blank=True, max_length=256, null=True, verbose_name='Descripcion')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to=galeria.models.imagenes.get_upload_img_name)),
                ('registro', models.DateTimeField(auto_now_add=True, verbose_name='Registrado')),
                ('estado', models.BooleanField(blank=True, max_length=256, verbose_name='Estado')),
                ('categoria', models.ForeignKey(blank=True, max_length=256, null=True, on_delete=django.db.models.deletion.CASCADE, to='galeria.categorias')),
            ],
        ),
    ]
