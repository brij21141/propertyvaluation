# Generated by Django 5.1 on 2024-10-30 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0014_archievereporterreport_archievedate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archievereporterreport',
            name='datecreated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='archievereporterreport',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]