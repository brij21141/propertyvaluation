# Generated by Django 5.1 on 2025-01-22 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0027_archievereporterreport_replat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archievereporterreport',
            name='add1',
            field=models.CharField(default='Gwalior', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='archievereporterreport',
            name='ladd1',
            field=models.CharField(default='Gwalior', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='reporterreport',
            name='add1',
            field=models.CharField(default='Gwalior', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='reporterreport',
            name='ladd1',
            field=models.CharField(default='Gwalior', max_length=250, null=True),
        ),
    ]
