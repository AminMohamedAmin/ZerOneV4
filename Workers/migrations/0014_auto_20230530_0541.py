# Generated by Django 3.2.5 on 2023-05-30 03:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Workers', '0013_auto_20230530_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerattendance',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 5, 30, 3, 39, 2, 760448, tzinfo=utc), verbose_name='تاريخ الحضور'),
        ),
        migrations.AlterField(
            model_name='workerpayment',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 5, 30, 3, 39, 2, 760448, tzinfo=utc), verbose_name='تاريخ السحب'),
        ),
        migrations.AlterField(
            model_name='workerproduction',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 5, 30, 3, 39, 2, 760448, tzinfo=utc), verbose_name='تاريخ الاستلام'),
        ),
    ]
