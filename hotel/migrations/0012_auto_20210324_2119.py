# Generated by Django 3.1.7 on 2021-03-25 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0011_auto_20210324_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='payment_status',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='payment_type',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='room',
        ),
        migrations.AddField(
            model_name='booking',
            name='room_id',
            field=models.IntegerField(null=True),
        ),
    ]
