# Generated by Django 4.0.7 on 2022-09-26 21:00

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0035_alter_catalogpage__content_catalog'),
    ]

    operations = [
        migrations.AddField(
            model_name='santillanasettings',
            name='terms_and_conditions',
            field=wagtail.fields.RichTextField(blank=True, verbose_name='Términos y condiciones'),
        ),
    ]
