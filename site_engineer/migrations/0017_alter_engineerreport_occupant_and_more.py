# Generated by Django 5.1 on 2024-10-26 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_engineer', '0016_remove_engineerreport_engineerholdcause'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineerreport',
            name='Occupant',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='engineerreport',
            name='east',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='engineerreport',
            name='ffarea',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='engineerreport',
            name='gfarea',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='engineerreport',
            name='landmark',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='engineerreport',
            name='landrate',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='engineerreport',
            name='north',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='engineerreport',
            name='priority',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='engineerreport',
            name='propertyage',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='engineerreport',
            name='roadwidth',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='engineerreport',
            name='sfarea',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='engineerreport',
            name='south',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='engineerreport',
            name='tfarea',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='engineerreport',
            name='visitinpresence',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='engineerreport',
            name='west',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
