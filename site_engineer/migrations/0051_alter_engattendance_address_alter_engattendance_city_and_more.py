# Generated by Django 5.1 on 2024-12-17 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_engineer', '0050_engattendance_outdatetinme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engattendance',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='engattendance',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='engattendance',
            name='country',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='engattendance',
            name='region',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='engattendance',
            name='zip',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
