# Generated by Django 3.1.1 on 2020-09-29 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_to_do_app', '0002_isdone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='isDone',
        ),
        migrations.AddField(
            model_name='todo',
            name='isDone',
            field=models.BooleanField(default=False),
        ),
    ]
