# Generated by Django 5.1 on 2024-11-04 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_engineer', '0022_archieveengineerreport_bankid'),
    ]

    operations = [
        migrations.AddField(
            model_name='engineerreport',
            name='bankid',
            field=models.IntegerField(null=True),
        ),
    ]