# Generated by Django 3.2.5 on 2023-06-13 06:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0017_alter_sellerpayments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerpayments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 13, 8, 37, 49, 872257), verbose_name='التاريخ'),
        ),
    ]
