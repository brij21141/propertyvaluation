# Generated by Django 5.1 on 2024-10-04 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0018_remove_document_reporterholdcause_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='receptionreport',
            name='bankid',
            field=models.IntegerField(null=True),
        ),
    ]
