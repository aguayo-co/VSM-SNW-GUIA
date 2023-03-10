# Generated by Django 4.0.6 on 2022-08-09 20:14

import commons.models.components
from django.db import migrations, models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("commons", "0013_detailproductpage_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="detailproductpage",
            name="idiom",
            field=models.CharField(
                blank=True,
                choices=[("en", "Inglés"), ("es", "Español")],
                default="es",
                max_length=10,
                null=True,
                verbose_name="Idioma",
            ),
        ),
        migrations.AlterField(
            model_name="detailproductpage",
            name="_thematic_content",
            field=wagtail.fields.StreamField(
                [
                    (
                        "thematic_content",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        label="Título", required=True
                                    ),
                                ),
                                (
                                    "items",
                                    wagtail.blocks.ListBlock(
                                        commons.models.components.ThematicContentItem,
                                        label="Items",
                                    ),
                                ),
                            ]
                        ),
                    )
                ],
                blank=True,
                null=True,
                use_json_field=None,
                verbose_name="Contenidos Temáticos",
            ),
        ),
    ]
