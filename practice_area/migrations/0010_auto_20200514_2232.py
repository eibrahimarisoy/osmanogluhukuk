# Generated by Django 2.2.7 on 2020-05-14 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice_area', '0009_practicearea_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='practicearea',
            options={'ordering': ['number']},
        ),
    ]
