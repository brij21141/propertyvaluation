# Generated by Django 5.1 on 2024-10-15 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_engineer', '0015_engineerreport_engineerholdcause'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='engineerreport',
            name='engineerholdcause',
        ),
    ]
