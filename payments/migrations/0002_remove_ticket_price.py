# Generated by Django 4.2.13 on 2024-07-01 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='price',
        ),
    ]
