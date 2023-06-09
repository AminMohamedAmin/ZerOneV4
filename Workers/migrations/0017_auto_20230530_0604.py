# Generated by Django 3.2.5 on 2023-05-30 04:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Workers', '0016_auto_20230530_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerattendance',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 5, 30, 4, 4, 5, 211044, tzinfo=utc), verbose_name='تاريخ الحضور'),
        ),
        migrations.AlterField(
            model_name='workerpayment',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 5, 30, 4, 4, 5, 212054, tzinfo=utc), verbose_name='تاريخ السحب'),
        ),
        migrations.AlterField(
            model_name='workerproduction',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 5, 30, 4, 4, 5, 212054, tzinfo=utc), verbose_name='تاريخ الاستلام'),
        ),
    ]
