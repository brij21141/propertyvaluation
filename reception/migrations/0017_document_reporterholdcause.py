# Generated by Django 5.1 on 2024-10-01 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0016_receptionreport_reporter'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='reporterholdcause',
            field=models.TextField(blank=True, null=True),
        ),
    ]
