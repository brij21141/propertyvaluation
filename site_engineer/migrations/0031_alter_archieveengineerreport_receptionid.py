# Generated by Django 5.1 on 2024-11-08 06:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0025_remove_archievereceptionreport_archievedate'),
        ('site_engineer', '0030_alter_archieveengineerreport_receptionid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archieveengineerreport',
            name='receptionid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reception.receptionreport'),
        ),
    ]
