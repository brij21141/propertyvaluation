# Generated by Django 5.1 on 2024-12-17 06:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_engineer', '0047_engattendance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='engattendance',
            old_name='datecreated',
            new_name='indatetinme',
        ),
        migrations.AddField(
            model_name='engattendance',
            name='outdatetinme',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
