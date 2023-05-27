# Generated by Django 3.2.5 on 2023-05-27 03:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Workers', '0006_merge_0004_auto_20230521_0029_0005_auto_20230519_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerattendance',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 5, 27, 3, 27, 35, 168103, tzinfo=utc), verbose_name='تاريخ الحضور'),
        ),
        migrations.AlterField(
            model_name='workerpayment',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 5, 27, 3, 27, 35, 168103, tzinfo=utc), verbose_name='تاريخ السحب'),
        ),
        migrations.AlterField(
            model_name='workerproduction',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 5, 27, 3, 27, 35, 168103, tzinfo=utc), verbose_name='تاريخ الاستلام'),
        ),
    ]