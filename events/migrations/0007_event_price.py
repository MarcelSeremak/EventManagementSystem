# Generated by Django 4.2.13 on 2024-06-30 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_event_tickets_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
