# Generated by Django 5.1 on 2024-12-06 06:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_engineer', '0043_floortemp'),
    ]

    operations = [
        migrations.AddField(
            model_name='floortemp',
            name='engreportid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='floors', to='site_engineer.engineerreport'),
        ),
    ]
