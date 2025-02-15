# Generated by Django 5.1 on 2024-09-03 10:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_engineer', '0004_engineerreport_reporter'),
    ]

    operations = [
        migrations.AddField(
            model_name='engineerreport',
            name='datecreated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='engineerreport',
            name='receptionid',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='engineerreport',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
