# Generated by Django 2.2.2 on 2019-07-31 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scouts', '0024_scouttaskassignmentrequest_auto_rejected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scouttaskcategory',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
