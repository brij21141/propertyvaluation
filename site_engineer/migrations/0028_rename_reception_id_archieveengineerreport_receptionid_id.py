# Generated by Django 5.1 on 2024-11-07 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_engineer', '0027_archieveengineerreport_reception_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='archieveengineerreport',
            old_name='reception_id',
            new_name='receptionid_id',
        ),
    ]
