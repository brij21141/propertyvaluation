# Generated by Django 5.1 on 2024-12-13 06:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0027_archievereceptionreport_npa_receptionreport_npa'),
        ('site_engineer', '0046_historyfloordetails'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EngAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicationnumber', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=30)),
                ('zip', models.CharField(max_length=6)),
                ('country', models.CharField(max_length=20)),
                ('lat', models.CharField(blank=True, max_length=200, null=True)),
                ('lng', models.CharField(blank=True, max_length=200, null=True)),
                ('placeid', models.CharField(blank=True, max_length=200, null=True)),
                ('datecreated', models.DateTimeField(auto_now_add=True)),
                ('receptionid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reception.receptionreport')),
                ('userdetailsid', models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
