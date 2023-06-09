# Generated by Django 4.2.1 on 2023-05-17 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logoo', models.ImageField(upload_to='Photo', verbose_name='Logo')),
                ('title', models.CharField(max_length=100, verbose_name='Title page')),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=100, verbose_name='Home name1')),
                ('name2', models.CharField(max_length=100, verbose_name='Home name2')),
                ('about', models.TextField(max_length=500, verbose_name='Home About')),
                ('img', models.ImageField(upload_to='Photo', verbose_name='Home Image')),
            ],
        ),
    ]
