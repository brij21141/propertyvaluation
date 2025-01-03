# Generated by Django 5.1 on 2024-10-07 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propval', '0008_banks_branch_banks_externalrate_banks_internalrate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='bankacno',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='bankname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='ifsc',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='pan',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='terms',
            field=models.TextField(blank=True, null=True),
        ),
    ]
