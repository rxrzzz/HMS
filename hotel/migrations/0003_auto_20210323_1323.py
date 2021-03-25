# Generated by Django 3.1.7 on 2021-03-23 20:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_booking_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to='hotel.customer'),
        ),
        migrations.AddField(
            model_name='booking',
            name='payment_status',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='booking',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to='hotel.booking'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_created',
            field=models.DateField(default=datetime.date(2021, 3, 23)),
        ),
        migrations.AlterField(
            model_name='manager',
            name='date_created',
            field=models.DateField(default=datetime.date(2021, 3, 23)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]