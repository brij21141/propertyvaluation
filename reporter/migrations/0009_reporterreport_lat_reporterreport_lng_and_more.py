# Generated by Django 5.1 on 2024-09-24 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0008_alter_reporterreport_userdetailsid'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporterreport',
            name='lat',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='reporterreport',
            name='lng',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='reporterreport',
            name='placeid',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
