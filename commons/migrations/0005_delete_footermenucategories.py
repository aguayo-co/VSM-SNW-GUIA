# Generated by Django 4.0.6 on 2022-07-21 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0003_remove_agflatmenuitem_footer_menu_category'),
        ('commons', '0004_footermenucategories'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FooterMenuCategories',
        ),
    ]
