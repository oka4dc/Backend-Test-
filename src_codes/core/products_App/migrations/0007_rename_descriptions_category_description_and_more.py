# Generated by Django 5.0.7 on 2024-07-24 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products_App', '0006_remove_products_product_id_category_descriptions_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Descriptions',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='Descriptions',
            new_name='Description',
        ),
    ]
