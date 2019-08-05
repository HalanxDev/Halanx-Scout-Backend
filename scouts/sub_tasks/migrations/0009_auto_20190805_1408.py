# Generated by Django 2.2.2 on 2019-08-05 08:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sub_tasks', '0008_auto_20190805_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertyonboardingdetail',
            name='scheduled_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 5, 8, 38, 21, 214405, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='propertyonboardingdetail',
            name='latitude',
            field=models.IntegerField(default=28.77),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='propertyonboardingdetail',
            name='longitude',
            field=models.IntegerField(default=77.77),
            preserve_default=False,
        ),
    ]
