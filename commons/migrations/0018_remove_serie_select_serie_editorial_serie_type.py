# Generated by Django 4.0.6 on 2022-08-11 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0017_alter_serie_options_serie_select_serie_editorial_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serie',
            name='select_serie_editorial',
        ),
        migrations.AddField(
            model_name='serie',
            name='type',
            field=models.CharField(choices=[('serie', 'Serie'), ('editorial', 'Editorial')], default='serie', max_length=255, verbose_name='Tipo'),
        ),
    ]