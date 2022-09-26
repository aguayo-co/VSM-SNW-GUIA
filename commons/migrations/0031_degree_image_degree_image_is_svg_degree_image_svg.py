# Generated by Django 4.0.6 on 2022-09-21 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailsvg", "0004_remove_svg_edit_code"),
        ("wagtailimages", "0024_index_image_file_hash"),
        ("commons", "0030_rename_idiom_detailproductpage_language_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="degree",
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
        migrations.AddField(
            model_name="degree",
            name="image_is_svg",
            field=models.BooleanField(
                blank=True, default=False, null=True, verbose_name="Usar imagen SVG"
            ),
        ),
        migrations.AddField(
            model_name="degree",
            name="image_svg",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailsvg.svg",
                verbose_name="Imagen",
            ),
        ),
    ]