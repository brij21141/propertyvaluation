# Generated by Django 5.1 on 2024-12-06 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_engineer', '0044_floortemp_engreportid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='floortemp',
            new_name='Floordetails',
        ),
    ]
