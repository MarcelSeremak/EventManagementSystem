# Generated by Django 4.2.13 on 2024-07-02 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_purchase'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Purchase',
        ),
    ]
