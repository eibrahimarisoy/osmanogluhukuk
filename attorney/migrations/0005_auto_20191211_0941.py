# Generated by Django 2.2.7 on 2019-12-11 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attorney', '0004_attorney_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attorney',
            name='surname',
        ),
        migrations.AlterField(
            model_name='attorney',
            name='name',
            field=models.CharField(max_length=50, verbose_name='ad ve soyad'),
        ),
    ]
