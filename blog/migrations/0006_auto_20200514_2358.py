# Generated by Django 2.2.7 on 2020-05-14 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200514_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='cover_image',
            field=models.FileField(blank=True, null=True, upload_to='blog', verbose_name='Fotoğraf'),
        ),
    ]