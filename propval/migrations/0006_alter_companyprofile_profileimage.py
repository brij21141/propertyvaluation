# Generated by Django 5.1 on 2024-09-27 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propval', '0005_companyprofile_country_companyprofile_zip_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='profileimage',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
    ]
