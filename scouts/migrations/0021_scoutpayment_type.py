# Generated by Django 2.2.2 on 2019-07-18 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scouts', '0020_scouttaskcategory_earning'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoutpayment',
            name='type',
            field=models.CharField(choices=[('withdrawal', 'Withdrawal'), ('deposit', 'Deposit')], default='withdrawal', max_length=30),
        ),
    ]