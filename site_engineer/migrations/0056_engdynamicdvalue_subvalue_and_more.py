# Generated by Django 5.1 on 2025-01-08 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_engineer', '0055_alter_engdynamicdvalue_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='engdynamicdvalue',
            name='subvalue',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='engdynamicdvalue',
            name='value',
            field=models.CharField(max_length=100, null=True),
        ),
    ]