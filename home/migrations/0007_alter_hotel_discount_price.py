# Generated by Django 4.1.3 on 2024-01-18 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_hotel_discount_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='discount_price',
            field=models.IntegerField(default=500),
        ),
    ]
