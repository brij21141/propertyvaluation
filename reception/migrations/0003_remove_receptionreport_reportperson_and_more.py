# Generated by Django 5.1 on 2024-08-27 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0002_receptionreport_engineer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receptionreport',
            name='reportperson',
        ),
        migrations.RemoveField(
            model_name='receptionreport',
            name='visitingperson',
        ),
    ]
