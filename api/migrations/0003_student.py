# Generated by Django 5.1.3 on 2024-12-10 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_programmer_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=10)),
                ('numero_ficha', models.PositiveSmallIntegerField()),
                ('formacion', models.CharField(max_length=30)),
                ('fecha_ingreso', models.DateField()),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
    ]
