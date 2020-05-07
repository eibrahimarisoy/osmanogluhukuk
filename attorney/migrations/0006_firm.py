# Generated by Django 2.2.7 on 2020-01-16 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attorney', '0005_auto_20191211_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Firma Adı')),
                ('address', models.CharField(max_length=250, verbose_name='Adres')),
                ('phone', models.IntegerField(max_length=11, verbose_name='Telefon')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('working_hour', models.CharField(max_length=150, verbose_name='Çalışma Saatleri')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]