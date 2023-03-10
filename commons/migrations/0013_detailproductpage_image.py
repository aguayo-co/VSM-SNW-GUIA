# Generated by Django 4.0.6 on 2022-08-09 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0024_index_image_file_hash"),
        ("commons", "0012_detailproductpage__thematic_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="detailproductpage",
            name="image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
                verbose_name="Imagen",
            ),
        ),
    ]
