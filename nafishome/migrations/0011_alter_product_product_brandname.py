# Generated by Django 5.0.6 on 2024-07-07 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nafishome', '0010_alter_product_product_brandname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_brandname',
            field=models.CharField(default='', max_length=100),
        ),
    ]
