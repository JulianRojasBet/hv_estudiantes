# Generated by Django 3.1.2 on 2020-10-31 16:05

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('fecha_limite', models.DateTimeField()),
                ('info_empresa', models.TextField()),
                ('perfil', models.TextField()),
                ('cant_vacantes', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('observaciones', models.TextField()),
                ('lugar_trabajo', models.CharField(max_length=100)),
                ('conocimientos', models.TextField()),
                ('experiencia', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('tipo_contrato', models.CharField(choices=[('IND', 'Término Indefinido'), ('FIJ', 'Término Fijo'), ('LAB', 'Labor'), ('OCA', 'Ocasional')], max_length=20)),
                ('contacto', models.CharField(max_length=50)),
                ('remuneracion', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('informacion', models.TextField()),
                ('funciones', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='usuario',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='categoria',
            field=models.CharField(blank=True, choices=[('PRE', 'Pregrado'), ('ESP', 'Especializacion'), ('MAE', 'Maestria'), ('POS', 'Posgrado')], max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='es_administrador',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='es_ofertante',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default=12345, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='tipo',
            field=models.CharField(blank=True, choices=[('EST', 'Estudiante'), ('EGR', 'Egresado')], max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(default='pipe', error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nacionalidad',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='sexo',
            field=models.CharField(blank=True, choices=[('F', 'Femenino'), ('M', 'Masculino'), ('X', 'No binario')], max_length=10, null=True),
        ),
    ]
