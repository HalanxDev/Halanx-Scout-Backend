# Generated by Django 2.2.2 on 2019-06-20 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scouts', '0012_scout_gcm_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scouttask',
            name='cancelled_by',
        ),
        migrations.CreateModel(
            name='ScoutTaskAssignmentRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('accepted', 'Accepted'), ('rejected', 'Rejected'), ('awaited', 'Awaited')], default='awaited', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('responded_at', models.DateTimeField(blank=True, null=True)),
                ('scout', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_assignment_requests', to='scouts.Scout')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assignment_requests', to='scouts.ScoutTask')),
            ],
        ),
    ]
