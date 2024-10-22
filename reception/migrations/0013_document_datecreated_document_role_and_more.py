# Generated by Django 5.1 on 2024-09-06 14:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0012_document_reception_idno'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='datecreated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='role',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='document',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]