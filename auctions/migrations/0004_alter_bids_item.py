# Generated by Django 3.2.7 on 2021-10-05 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20211005_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bids',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.listings'),
        ),
    ]