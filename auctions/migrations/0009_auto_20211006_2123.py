# Generated by Django 3.2.7 on 2021-10-06 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_listings_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bids',
            name='item',
        ),
        migrations.AddField(
            model_name='bids',
            name='item',
            field=models.ManyToManyField(default=1, related_name='bids', to='auctions.Listings'),
        ),
        migrations.RemoveField(
            model_name='comments',
            name='item',
        ),
        migrations.AddField(
            model_name='comments',
            name='item',
            field=models.ManyToManyField(default=1, related_name='comments', to='auctions.Listings'),
        ),
    ]
