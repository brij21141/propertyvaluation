# Generated by Django 5.1 on 2024-11-07 15:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0025_remove_archievereceptionreport_archievedate'),
        ('reporter', '0018_archievereporterreport_receptionid_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archievereporterreport',
            name='receptionid_id',
        ),
        migrations.AddField(
            model_name='archievereporterreport',
            name='receptionid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reception.receptionreport'),
        ),
    ]
