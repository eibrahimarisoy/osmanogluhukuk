# Generated by Django 2.2.7 on 2019-12-11 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attorney', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lawyers',
            new_name='Attorney',
        ),
    ]
