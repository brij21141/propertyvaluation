# Generated by Django 5.1 on 2024-11-08 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0025_remove_archievereceptionreport_archievedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='archievereceptionreport',
            name='engid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='archievereceptionreport',
            name='repid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='receptionreport',
            name='engid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='receptionreport',
            name='repid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
