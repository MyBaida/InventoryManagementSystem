# Generated by Django 4.2.7 on 2023-11-26 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapp', '0002_alter_product_category_alter_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
