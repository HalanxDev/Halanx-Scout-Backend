# Generated by Django 2.2.2 on 2019-06-08 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scouts', '0006_scoutnotification_scoutnotificationcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoutnotification',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notifications', to='scouts.ScoutNotificationCategory'),
        ),
    ]
