# Generated by Django 4.0.7 on 2022-09-26 14:43

import commons.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0034_delete_thankyoupage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogpage',
            name='_content_catalog',
            field=commons.models.fields.CatalogPageStreamField(blank=True, null=True, use_json_field=None, verbose_name='Contenido'),
        ),
    ]