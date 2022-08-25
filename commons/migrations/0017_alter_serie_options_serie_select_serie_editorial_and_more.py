# Generated by Django 4.0.6 on 2022-08-11 00:47

import commons.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0024_index_image_file_hash"),
        ("commons", "0016_detailproductpage_audio_detailproductpage_posters_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="serie",
            options={
                "verbose_name": "Serie o sello editorial",
                "verbose_name_plural": "Series o sellos editoriales",
            },
        ),
        migrations.AddField(
            model_name="serie",
            name="select_serie_editorial",
            field=models.CharField(
                choices=[("serie", "Serie"), ("editorial", "Editorial")],
                default=None,
                max_length=255,
                verbose_name="serie o editorial",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="detailproductpage",
            name="_content_detail_product",
            field=commons.models.fields.DetailProductStreamField(
                blank=True, null=True, use_json_field=None, verbose_name="Contenido"
            ),
        ),
        migrations.AlterField(
            model_name="detailproductpage",
            name="image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
                verbose_name="Imagen del Libro",
            ),
        ),
        migrations.AlterField(
            model_name="detailproductpage",
            name="short_description",
            field=models.TextField(
                blank=True, null=True, verbose_name="Descripción Corta"
            ),
        ),
    ]
