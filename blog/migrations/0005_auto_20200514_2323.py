# Generated by Django 2.2.7 on 2020-05-14 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpost_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-created_date']},
        ),
    ]
