# Generated by Django 5.1 on 2024-12-02 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_engineer', '0038_historyengineerreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='historyengineerreport',
            name='old_id',
            field=models.IntegerField(null=True),
        ),
    ]