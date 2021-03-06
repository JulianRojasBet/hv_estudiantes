# Generated by Django 3.1.2 on 2020-10-22 19:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=13)),
                ('direccion', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino'), ('X', 'No binario')], max_length=10)),
                ('nacionalidad', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Reconocimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('lugar', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reconocimiento', to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('titulo_publicacion', models.TextField()),
                ('isbn', models.CharField(max_length=13, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(13)])),
                ('issn', models.CharField(max_length=8, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(8)])),
                ('editorial', models.CharField(max_length=50)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='publicacion', to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('habla', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('escribe', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('lee', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('escucha', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='idioma', to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='HojaVida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('experiencia', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('otra_info', models.TextField()),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='FormacionComplementaria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('lugar', models.TextField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='formacion_complementaria', to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='FormacionAcademica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('lugar', models.CharField(max_length=50)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('titulo_trabajo', models.TextField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='formacion_academica', to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='ExperienciaProfesional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=50)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('dedicacion_semanal', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='experiencia_profesional', to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='AreaActuacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='area_actuacion', to='core.usuario')),
            ],
        ),
    ]
