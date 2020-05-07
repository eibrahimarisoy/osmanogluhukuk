# Generated by Django 2.2.7 on 2020-05-07 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attorney', '0010_auto_20200130_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='firm',
            old_name='cover_image',
            new_name='navbar_image',
        ),
        migrations.AddField(
            model_name='firm',
            name='footer_image',
            field=models.ImageField(blank=True, null=True, upload_to='logo', verbose_name='200*75 px'),
        ),
    ]
