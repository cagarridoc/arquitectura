# Generated by Django 4.2.6 on 2023-10-12 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='condicionSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoCondicionSocial', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_hospital', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Muerte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaMuerte', models.DateField()),
                ('causaMuerte', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePaciente', models.CharField(max_length=50)),
                ('sNombrePaciente', models.CharField(max_length=50)),
                ('apPaterno', models.CharField(max_length=50)),
                ('apMaterno', models.CharField(max_length=50)),
                ('edad', models.PositiveBigIntegerField()),
                ('fechaMuerte', models.DateField()),
                ('generoPaciente', models.CharField(max_length=1)),
                ('fecNacPaciente', models.DateField()),
            ],
        ),
    ]
