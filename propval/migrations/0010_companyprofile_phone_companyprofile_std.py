# Generated by Django 5.1 on 2024-10-07 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propval', '0009_companyprofile_bankacno_companyprofile_bankname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='std',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]