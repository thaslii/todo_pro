# Generated by Django 4.2.6 on 2023-10-16 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1995-03-23'),
            preserve_default=False,
        ),
    ]
