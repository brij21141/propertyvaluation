# Generated by Django 5.1 on 2025-01-07 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_engineer', '0054_historyengdynamicdvalue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engdynamicdvalue',
            name='value',
            field=models.TextField(null=True),
        ),
    ]
