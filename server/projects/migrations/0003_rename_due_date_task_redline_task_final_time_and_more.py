# Generated by Django 5.1.7 on 2025-04-03 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_is_active_alter_project_client_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='due_date',
            new_name='redline',
        ),
        migrations.AddField(
            model_name='task',
            name='final_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='initial_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
