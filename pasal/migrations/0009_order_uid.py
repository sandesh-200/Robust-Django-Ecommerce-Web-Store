# Generated by Django 5.0.3 on 2024-06-23 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pasal', '0008_order_date_bill'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='uid',
            field=models.CharField(default='', max_length=300),
        ),
    ]
