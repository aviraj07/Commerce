# Generated by Django 3.2.7 on 2021-10-05 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bids_comments_listings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bids',
            name='item',
        ),
        migrations.AddField(
            model_name='bids',
            name='item',
            field=models.ForeignKey(default='000000', on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.listings'),
        ),
    ]
