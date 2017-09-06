# Generated by Django 2.0 on 2017-09-06 03:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0006_record'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='record',
            options={'verbose_name': '记录', 'verbose_name_plural': '记录'},
        ),
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 6, 3, 53, 45, 805770, tzinfo=utc), verbose_name='记录时间'),
        ),
        migrations.AlterField(
            model_name='record',
            name='strength',
            field=models.CharField(max_length=64, verbose_name='强度'),
        ),
        migrations.AlterField(
            model_name='record',
            name='way',
            field=models.CharField(max_length=32, verbose_name='运动方式'),
        ),
    ]
