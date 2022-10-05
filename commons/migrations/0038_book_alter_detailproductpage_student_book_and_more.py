# Generated by Django 4.0.7 on 2022-09-28 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0012_uploadeddocument'),
        ('commons', '0037_santillanasettings_key_recaptcha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document', verbose_name='Documento')),
                ('external_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='commons.externalredirect', verbose_name='Libro externo')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
            },
        ),
        migrations.AlterField(
            model_name='detailproductpage',
            name='student_book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='commons.book', verbose_name='Libro del Estudiante'),
        ),
        migrations.AlterField(
            model_name='detailproductpage',
            name='teacher_book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='commons.book', verbose_name='Libro del docente (Español)'),
        ),
        migrations.AlterField(
            model_name='detailproductpage',
            name='teacher_book_english',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='commons.book', verbose_name='Libro del docente (Inglés)'),
        ),
    ]
