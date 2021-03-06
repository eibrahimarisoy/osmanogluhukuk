# Generated by Django 2.2.7 on 2020-05-14 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_area', '0010_auto_20200514_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicearea',
            name='cover_image',
            field=models.FileField(blank=True, null=True, upload_to='practice_area', verbose_name='Fotoğraf'),
        ),
        migrations.AlterField(
            model_name='practicearea',
            name='summary',
            field=models.CharField(default='Sed ut perspiciatis unde omnis iste natus                             error sit voluptatem accusantium doloremque                             laudantium, totam rem aperiam, eaque ipsa quae                             ab illo inventore veritatis et quasi architecto                             beatae vitae dicta sunt explicabo.', max_length=250),
        ),
    ]
