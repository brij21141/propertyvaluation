# Generated by Django 5.1 on 2024-11-08 05:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0025_remove_archievereceptionreport_archievedate'),
        ('reporter', '0019_remove_archievereporterreport_receptionid_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archievereporterreport',
            name='receptionid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reception.archievereceptionreport'),
        ),
    ]
