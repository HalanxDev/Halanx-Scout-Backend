# Generated by Django 2.2.2 on 2019-08-03 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_tasks', '0006_propertyonboardinghouseaddress_propertyonboardinghouseamenity_propertyonboardinghousebasicdetail_pro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyonboardinghouseaddress',
            name='street_address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
