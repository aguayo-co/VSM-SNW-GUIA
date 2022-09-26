# Generated by Django 4.0.6 on 2022-09-21 21:07

import commons.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("commons", "0029_rename__thematic_content_detailproductpage_thematic_content"),
    ]

    operations = [
        migrations.RenameField(
            model_name="detailproductpage",
            old_name="idiom",
            new_name="language",
        ),
        migrations.AddField(
            model_name="coursedetailpage",
            name="footer_content",
            field=commons.models.fields.CourseDetailStreamField(
                blank=True, null=True, use_json_field=None, verbose_name="Contenido"
            ),
        ),
        migrations.AddField(
            model_name="detailproductpage",
            name="campo_formacion",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Campo formación"
            ),
        ),
        migrations.AlterField(
            model_name="coursedetailpage",
            name="_content_course_detail",
            field=commons.models.fields.DetailProductIntroStreamField(
                blank=True, null=True, use_json_field=None, verbose_name="Intro"
            ),
        ),
    ]