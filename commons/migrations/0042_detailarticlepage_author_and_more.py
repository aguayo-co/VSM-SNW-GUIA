# Generated by Django 4.0.7 on 2022-10-05 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0041_santillanasettings_contact_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailarticlepage',
            name='author',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Autor'),
        ),
        migrations.AddField(
            model_name='detailarticlepage',
            name='reading_time',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Tiempo de lectura'),
        ),
    ]
