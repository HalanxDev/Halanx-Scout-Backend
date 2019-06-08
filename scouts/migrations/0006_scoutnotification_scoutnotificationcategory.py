# Generated by Django 2.2.2 on 2019-06-08 09:04

import common.utils
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('scouts', '0005_auto_20190608_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScoutNotificationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, null=True, upload_to=common.utils.get_notification_category_image_upload_path)),
            ],
            options={
                'verbose_name_plural': 'Scout notification categories',
            },
        ),
        migrations.CreateModel(
            name='ScoutNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(blank=True, max_length=200, null=True)),
                ('payload', jsonfield.fields.JSONField(blank=True, null=True)),
                ('seen', models.BooleanField(default=False)),
                ('display', models.BooleanField(default=True)),
                ('scout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='scouts.Scout')),
            ],
            options={
                'ordering': ('-timestamp',),
                'abstract': False,
            },
        ),
    ]
