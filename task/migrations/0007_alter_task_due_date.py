# Generated by Django 5.0.7 on 2025-03-11 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
