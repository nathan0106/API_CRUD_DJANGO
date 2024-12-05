# Generated by Django 5.1.3 on 2024-12-03 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='programmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=30)),
                ('age', models.PositiveSmallIntegerField(default=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]