# Generated by Django 5.0.6 on 2024-08-02 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nafishome', '0012_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='optional_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]