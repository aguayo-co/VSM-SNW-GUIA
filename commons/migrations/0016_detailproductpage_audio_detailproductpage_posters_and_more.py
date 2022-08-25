# Generated by Django 4.0.6 on 2022-08-09 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wagtaildocs", "0012_uploadeddocument"),
        ("commons", "0015_detailproductpage_author_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="detailproductpage",
            name="audio",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtaildocs.document",
                verbose_name="Audios",
            ),
        ),
        migrations.AddField(
            model_name="detailproductpage",
            name="posters",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtaildocs.document",
                verbose_name="Posters",
            ),
        ),
        migrations.AddField(
            model_name="detailproductpage",
            name="reader",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtaildocs.document",
                verbose_name="Reader",
            ),
        ),
        migrations.AddField(
            model_name="detailproductpage",
            name="teacher_book_english",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtaildocs.document",
                verbose_name="Libro del docente (Inglés)",
            ),
        ),
        migrations.AlterField(
            model_name="detailproductpage",
            name="serie",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="commons.serie",
                verbose_name="Serie o Editorial",
            ),
        ),
        migrations.AlterField(
            model_name="detailproductpage",
            name="teacher_book",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtaildocs.document",
                verbose_name="Libro del docente (Español)",
            ),
        ),
    ]
