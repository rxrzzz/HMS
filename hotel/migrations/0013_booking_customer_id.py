# Generated by Django 3.1.7 on 2021-03-25 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0012_auto_20210324_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='customer_id',
            field=models.IntegerField(null=True),
        ),
    ]
