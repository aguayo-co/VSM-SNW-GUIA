# Generated by Django 4.0.6 on 2022-08-09 02:55

import commons.models.components
from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("commons", "0011_homepage_hero_alter_basepage__content_base_and_more"),
    ]

    operations = [
        migrations.AddField(
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
                verbose_name="Contenido",
            ),
        ),
    ]
