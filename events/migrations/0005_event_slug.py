# Generated by Django 4.2.13 on 2024-05-26 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
