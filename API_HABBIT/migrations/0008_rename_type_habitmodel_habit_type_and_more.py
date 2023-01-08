# Generated by Django 4.1.5 on 2023-01-07 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API_HABBIT', '0007_rename_habit_habitmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habitmodel',
            old_name='type',
            new_name='habit_type',
        ),
        migrations.RenameField(
            model_name='habitmodel',
            old_name='Question',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='habitmodel',
            old_name='Title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='habitmodel',
            name='completed',
        ),
    ]
