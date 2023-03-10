# Generated by Django 4.0.6 on 2022-07-19 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("commons", "0004_footermenucategories"),
        ("menus", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="agflatmenuitem",
            name="footer_menu_category",
            field=models.ForeignKey(
                default=None,
                help_text="Categoría asignada, valido únicamente en el Footer Menú",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="commons.footermenucategories",
            ),
            preserve_default=False,
        ),
    ]
