# Generated by Django 5.1 on 2024-10-15 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0019_receptionreport_bankid'),
    ]

    operations = [
        migrations.AddField(
            model_name='receptionreport',
            name='engineerholdcause',
            field=models.TextField(blank=True, null=True),
        ),
    ]