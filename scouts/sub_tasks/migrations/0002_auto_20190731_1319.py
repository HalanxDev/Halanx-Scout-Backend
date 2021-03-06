# Generated by Django 2.2.2 on 2019-07-31 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scouts', '0025_auto_20190731_1230'),
        ('sub_tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moveoutsubtask',
            name='parent_subtask',
        ),
        migrations.RemoveField(
            model_name='moveoutsubtask',
            name='parent_task',
        ),
        migrations.AddField(
            model_name='moveoutsubtask',
            name='parent_subtask_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scouts.ScoutSubTaskCategory'),
        ),
        migrations.AddField(
            model_name='moveoutsubtask',
            name='parent_task_category',
            field=models.ForeignKey(default='Move Out', null=True, on_delete=django.db.models.deletion.SET_NULL, to='scouts.ScoutTaskCategory', to_field='name'),
        ),
    ]
