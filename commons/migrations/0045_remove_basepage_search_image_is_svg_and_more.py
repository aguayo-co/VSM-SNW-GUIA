# Generated by Django 4.0.7 on 2022-10-24 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0044_alter_detailarticlepage_footer_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basepage',
            name='search_image_is_svg',
        ),
        migrations.RemoveField(
            model_name='basepage',
            name='search_image_svg',
        ),
        migrations.RemoveField(
            model_name='degree',
            name='image_is_svg',
        ),
        migrations.RemoveField(
            model_name='degree',
            name='image_svg',
        ),
        migrations.RemoveField(
            model_name='detailproductpage',
            name='image_is_svg',
        ),
        migrations.RemoveField(
            model_name='detailproductpage',
            name='image_svg',
        ),
        migrations.RemoveField(
            model_name='santillanasettings',
            name='logo_footer_is_svg',
        ),
        migrations.RemoveField(
            model_name='santillanasettings',
            name='logo_footer_svg',
        ),
        migrations.RemoveField(
            model_name='santillanasettings',
            name='logo_is_svg',
        ),
        migrations.RemoveField(
            model_name='santillanasettings',
            name='logo_svg',
        ),
        migrations.RemoveField(
            model_name='serie',
            name='image_is_svg',
        ),
        migrations.RemoveField(
            model_name='serie',
            name='image_svg',
        ),
    ]
