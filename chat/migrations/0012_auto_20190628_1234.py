# Generated by Django 2.2.2 on 2019-06-28 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0011_auto_20190628_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socketclient',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='socket_clients', to='chat.Participant'),
        ),
    ]