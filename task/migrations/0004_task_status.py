# Generated by Django 5.0.7 on 2025-02-24 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_alter_task_date_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('notdone', 'notdone'), ('inprogress', 'inprogress'), ('complete', 'complete')], max_length=255, null=True),
        ),
    ]
