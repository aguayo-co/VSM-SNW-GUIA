# Generated by Django 4.0.7 on 2022-09-26 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_remove_formfield_custom_terms_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formfield',
            name='field_type',
            field=models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('multiselect', 'Multiple select'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time'), ('hidden', 'Hidden field'), ('terms_and_conditions', 'Términos y condiciones')], max_length=32, verbose_name='field type'),
        ),
    ]
