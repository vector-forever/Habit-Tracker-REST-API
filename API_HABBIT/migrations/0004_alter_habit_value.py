# Generated by Django 4.1.5 on 2023-01-06 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API_HABBIT', '0003_alter_habit_type_alter_habit_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='value',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True),
        ),
    ]
