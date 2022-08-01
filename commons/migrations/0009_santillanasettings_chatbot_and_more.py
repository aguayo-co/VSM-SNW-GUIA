# Generated by Django 4.0.6 on 2022-08-01 17:43

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('commons', '0008_rename_degree_detailproductpage_grade_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='santillanasettings',
            name='chatbot',
            field=models.TextField(blank=True, verbose_name='Chatbot'),
        ),
        migrations.AlterField(
            model_name='santillanasettings',
            name='cookies_text',
            field=wagtail.fields.RichTextField(blank=True, verbose_name='Texto Cookies'),
        ),
        migrations.AlterField(
            model_name='santillanasettings',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='santillanasettings',
            name='logo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.image', verbose_name='Logo del sitio'),
        ),
        migrations.AlterField(
            model_name='santillanasettings',
            name='logo_footer',
            field=models.ForeignKey(help_text='Logo alternativo que se utiliza en lugares de contraste oscuro, como el footer.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Logo del footer'),
        ),
        migrations.AlterField(
            model_name='santillanasettings',
            name='logo_url',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.page', verbose_name='URL Logo'),
        ),
        migrations.AlterField(
            model_name='santillanasettings',
            name='phone',
            field=models.TextField(verbose_name='Teléfono'),
        ),
        migrations.DeleteModel(
            name='ThematicHomePage',
        ),
    ]
