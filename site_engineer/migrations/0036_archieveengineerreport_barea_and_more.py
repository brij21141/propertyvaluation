# Generated by Django 5.1 on 2024-11-18 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_engineer', '0035_remove_archieveengineerreport_receptiontempid'),
    ]

    operations = [
        migrations.AddField(
            model_name='archieveengineerreport',
            name='barea',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='archieveengineerreport',
            name='frarea',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='archieveengineerreport',
            name='fvarea',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='archieveengineerreport',
            name='sxarea',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
