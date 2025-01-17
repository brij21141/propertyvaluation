# Generated by Django 5.1 on 2024-10-07 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propval', '0010_companyprofile_phone_companyprofile_std'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='add1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='add2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='country',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='region',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='zip',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
