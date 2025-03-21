# Generated by Django 5.1.6 on 2025-02-23 20:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('due_date', models.DateField()),
                ('status', models.CharField(choices=[('notdone', 'notdone'), ('inprogress', 'inprogress'), ('done', 'done')], max_length=255)),
                ('comments', models.TextField()),
                ('prize_earned', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_prayed', models.DateField()),
                ('comments', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sprint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.sprint')),
            ],
        ),
        migrations.CreateModel(
            name='Meditation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_meditated', models.DateField()),
                ('minutes_spent', models.IntegerField(default=0)),
                ('comments', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sprint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.sprint')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('due_date', models.DateField()),
                ('date_completed', models.DateField()),
                ('official_due_by', models.DateField(blank=True, null=True)),
                ('late_fine', models.IntegerField(blank=True, null=True)),
                ('priority', models.CharField(choices=[('high', 'high'), ('medium', 'medium'), ('low', 'low')], max_length=255)),
                ('comments', models.TextField(blank=True, null=True)),
                ('task_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sprint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.sprint')),
            ],
        ),
    ]
