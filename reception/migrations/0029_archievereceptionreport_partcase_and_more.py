# Generated by Django 5.1 on 2025-01-22 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0028_recdynamicdvalue'),
    ]

    operations = [
        migrations.AddField(
            model_name='archievereceptionreport',
            name='partcase',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='receptionreport',
            name='partcase',
            field=models.BooleanField(default=False),
        ),
    ]