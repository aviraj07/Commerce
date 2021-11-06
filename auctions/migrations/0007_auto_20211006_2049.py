# Generated by Django 3.2.7 on 2021-10-06 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20211006_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='category',
            field=models.CharField(default=None, max_length=64),
        ),
        migrations.AddField(
            model_name='listings',
            name='url',
            field=models.URLField(default=None),
        ),
    ]
