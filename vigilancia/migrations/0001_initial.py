# Generated by Django 4.1.1 on 2022-11-29 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('unidad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='universotratamientofocal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('universo', models.CharField(blank=True, max_length=200, null=True, verbose_name='Universo')),
                ('plandiario', models.CharField(blank=True, max_length=200, null=True, verbose_name='Plan Diario')),
                ('unidad', models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.CASCADE, to='unidad.unidad')),
            ],
        ),
        migrations.CreateModel(
            name='universotratamientoadulticida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('universo', models.CharField(blank=True, max_length=200, null=True, verbose_name='Universo')),
                ('plandiario', models.CharField(blank=True, max_length=200, null=True, verbose_name='Plan Diario')),
                ('unidad', models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.CASCADE, to='unidad.unidad')),
            ],
        ),
        migrations.CreateModel(
            name='tratamientofocal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depoinspecciondos', models.CharField(blank=True, max_length=200, null=True, verbose_name='Locales Inspeccionados  ')),
                ('depocerrados', models.CharField(blank=True, max_length=200, null=True, verbose_name='Locales Cerrados')),
                ('depositostotal', models.CharField(blank=True, max_length=200, null=True, verbose_name='Depositos Totales')),
                ('depositospositivos', models.CharField(blank=True, max_length=200, null=True, verbose_name='Depositos Positivos')),
                ('innaexistentes', models.CharField(blank=True, max_length=200, null=True, verbose_name='Inaccesibles Existentes')),
                ('innainspeccionados', models.CharField(blank=True, max_length=200, null=True, verbose_name='Inaccesibles Inspeccionados')),
                ('localpoadultos', models.CharField(blank=True, max_length=200, null=True, verbose_name='Local + Adultos')),
                ('localpolarv', models.CharField(blank=True, max_length=200, null=True, verbose_name='Local + Larvas o Pupas')),
                ('localpototal', models.CharField(blank=True, max_length=200, null=True, verbose_name='Local + Totales')),
                ('localpoindcasa', models.CharField(blank=True, max_length=200, null=True, verbose_name='Local + Indice por Casa')),
                ('localpoindbetau', models.CharField(blank=True, max_length=200, null=True, verbose_name='Local + Indice Betau')),
                ('actualizacion', models.DateTimeField(auto_now_add=True, verbose_name='Hora de Actualizacion ')),
                ('unidad', models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.CASCADE, to='unidad.unidad')),
                ('universo', models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.CASCADE, to='vigilancia.universotratamientofocal')),
            ],
        ),
        migrations.CreateModel(
            name='tratamientoadulticida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plandiario', models.CharField(blank=True, max_length=200, null=True, verbose_name='Plan Diario')),
                ('tratadas', models.CharField(blank=True, max_length=200, null=True, verbose_name='Tratadas')),
                ('cerrados', models.CharField(blank=True, max_length=200, null=True, verbose_name='Cerradas')),
                ('manzanasuniverso', models.CharField(blank=True, max_length=200, null=True, verbose_name='Universo Manzanas')),
                ('manzanastratadas', models.CharField(blank=True, max_length=200, null=True, verbose_name='Manzanas Tratadas')),
                ('localuniverso', models.CharField(blank=True, max_length=200, null=True, verbose_name='Universo de Locales')),
                ('localratados', models.CharField(blank=True, max_length=200, null=True, verbose_name='Local Tratados')),
                ('localcerradas', models.CharField(blank=True, max_length=200, null=True, verbose_name='Local Cerradas')),
                ('actualizacion', models.DateTimeField(auto_now_add=True, verbose_name='Hora de Actualizacion ')),
                ('unidad', models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.CASCADE, to='unidad.unidad')),
                ('universo', models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.CASCADE, to='vigilancia.universotratamientoadulticida')),
            ],
        ),
        migrations.CreateModel(
            name='recursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rrhhhombres', models.CharField(blank=True, max_length=200, null=True, verbose_name='Total de Hombres')),
                ('rrhhhombrestrabajando', models.CharField(blank=True, max_length=200, null=True, verbose_name='Hombres Trabajando')),
                ('equipostotal', models.CharField(blank=True, max_length=200, null=True, verbose_name='Total de Equipos ')),
                ('equipostrabajando', models.CharField(blank=True, max_length=200, null=True, verbose_name='Equipos Trabajando')),
                ('equiposnosalieron', models.CharField(blank=True, max_length=200, null=True, verbose_name='Equipos que No salieron')),
                ('equiposrotos', models.CharField(blank=True, max_length=200, null=True, verbose_name='Equipos Rotos')),
                ('actualizacion', models.DateTimeField(auto_now_add=True, verbose_name='Hora de Actualizacion ')),
                ('unidad', models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.CASCADE, to='unidad.unidad')),
            ],
        ),
        migrations.CreateModel(
            name='centrospriorizados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciplan', models.CharField(blank=True, max_length=200, null=True, verbose_name='Centros Inspeccionados Plan')),
                ('cireal', models.CharField(blank=True, max_length=200, null=True, verbose_name='Centros Inspeccionados Real')),
                ('larvitrampasinstaladas', models.CharField(blank=True, max_length=200, null=True, verbose_name='Larvitrampas Instaladas')),
                ('larvitrampaspositivas', models.CharField(blank=True, max_length=200, null=True, verbose_name='Larvitrampas Positivas')),
                ('epaaeg', models.CharField(blank=True, max_length=200, null=True, verbose_name='Especie Predominante Aedes Aegipti')),
                ('epaalb', models.CharField(blank=True, max_length=200, null=True, verbose_name='Especie Predominante Aedes Albupico')),
                ('epatan', models.CharField(blank=True, max_length=200, null=True, verbose_name='Especie Predominante Aedes Taen.')),
                ('epaalbm', models.CharField(blank=True, max_length=200, null=True, verbose_name='Especie Predominante Aedes Almbom')),
                ('epoe', models.CharField(blank=True, max_length=200, null=True, verbose_name='Otras Especies predominantes')),
                ('otros', models.CharField(blank=True, max_length=200, null=True, verbose_name='Otros Vectores')),
                ('moscas', models.CharField(blank=True, max_length=200, null=True, verbose_name='Moscas')),
                ('cucarachas', models.CharField(blank=True, max_length=200, null=True, verbose_name='Cucarachas')),
                ('roedores', models.CharField(blank=True, max_length=200, null=True, verbose_name='Roedores')),
                ('larvasgeneral', models.CharField(blank=True, max_length=200, null=True, verbose_name='Larvas general')),
                ('adulreposo', models.CharField(blank=True, max_length=200, null=True, verbose_name='Adultos en Reposo')),
                ('encebohumano', models.CharField(blank=True, max_length=200, null=True, verbose_name='En Cebo Humano')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('actualizacion', models.DateTimeField(auto_now_add=True, verbose_name='Hora de Actualizacion')),
                ('unidad', models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.CASCADE, to='unidad.unidad')),
            ],
        ),
        migrations.CreateModel(
            name='centrospositivos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre')),
                ('organismo', models.CharField(blank=True, max_length=200, null=True, verbose_name='Organismo')),
                ('direccion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Direccion')),
                ('depositos', models.CharField(blank=True, max_length=200, null=True, verbose_name='Depositos')),
                ('clasificacion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Clasificacion')),
                ('actualizacion', models.DateTimeField(auto_now_add=True, verbose_name='Hora de Actualizacion ')),
                ('unidad', models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.CASCADE, to='unidad.unidad')),
            ],
        ),
        migrations.CreateModel(
            name='centroscerrados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre')),
                ('organismo', models.CharField(blank=True, max_length=200, null=True, verbose_name='Organismo')),
                ('direccion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Direccion')),
                ('actualizacion', models.DateTimeField(auto_now_add=True, verbose_name='Hora de Actualizacion ')),
                ('unidad', models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.CASCADE, to='unidad.unidad')),
            ],
        ),
        migrations.CreateModel(
            name='albopictus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('focos', models.CharField(blank=True, max_length=200, null=True, verbose_name='Focos')),
                ('tbajo', models.CharField(blank=True, max_length=200, null=True, verbose_name='Tanques Bajos')),
                ('telev', models.CharField(blank=True, max_length=200, null=True, verbose_name='Tanques Elevados')),
                ('ciste', models.CharField(blank=True, max_length=200, null=True, verbose_name='Cisternas')),
                ('a4odep', models.CharField(blank=True, max_length=200, null=True, verbose_name='A4')),
                ('artnodestruible', models.CharField(blank=True, max_length=200, null=True, verbose_name='Artesanales No Destruibles')),
                ('artdestruible', models.CharField(blank=True, max_length=200, null=True, verbose_name='Artesanales Destruibles')),
                ('naturales', models.CharField(blank=True, max_length=200, null=True, verbose_name='Naturales')),
                ('eresliq', models.CharField(blank=True, max_length=200, null=True, verbose_name='Residuos L')),
                ('depvigi', models.CharField(blank=True, max_length=200, null=True, verbose_name='Depositos Vigilancia')),
                ('adultos', models.CharField(blank=True, max_length=200, null=True, verbose_name='Adultos')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('actualizacion', models.DateTimeField(auto_now_add=True, verbose_name='Hora de Actualizacion')),
                ('unidad', models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.CASCADE, to='unidad.unidad')),
            ],
        ),
    ]
