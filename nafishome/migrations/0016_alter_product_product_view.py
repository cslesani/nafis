# Generated by Django 5.0.6 on 2024-08-03 08:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nafishome', '0015_diameter_inseam_width_delete_tirecategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_view',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nafishome.inseam'),
        ),
    ]
