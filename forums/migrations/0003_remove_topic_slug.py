# Generated by Django 3.2.8 on 2021-11-19 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0002_auto_20211119_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='slug',
        ),
    ]
