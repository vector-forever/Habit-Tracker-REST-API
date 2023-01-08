# Generated by Django 4.1.5 on 2023-01-07 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API_HABBIT', '0012_alter_habitresponse_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitresponse',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterUniqueTogether(
            name='habitresponse',
            unique_together={('habit_id', 'date')},
        ),
    ]
