# Generated by Django 5.0.6 on 2024-08-03 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nafishome', '0016_alter_product_product_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_view',
            field=models.IntegerField(default=0),
        ),
    ]
