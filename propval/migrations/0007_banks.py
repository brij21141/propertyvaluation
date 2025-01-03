# Generated by Django 5.1 on 2024-09-29 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propval', '0006_alter_companyprofile_profileimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('add1', models.TextField(blank=True, null=True)),
                ('add2', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('zip', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=15, null=True)),
                ('std', models.CharField(blank=True, max_length=4, null=True)),
                ('landline', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('gstin', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
