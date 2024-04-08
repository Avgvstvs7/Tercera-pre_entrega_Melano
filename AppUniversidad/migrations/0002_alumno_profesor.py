# Generated by Django 5.0.3 on 2024-04-07 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUniversidad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumno', models.CharField(max_length=40)),
                ('curso', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('curso', models.CharField(max_length=40)),
            ],
        ),
    ]
