# Generated by Django 5.1 on 2024-08-26 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receptionreport',
            name='engineer',
            field=models.CharField(max_length=10, null=True),
        ),
    ]