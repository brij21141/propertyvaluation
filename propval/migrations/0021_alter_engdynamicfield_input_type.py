# Generated by Django 5.1 on 2024-12-24 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propval', '0020_alter_engdynamicfield_input_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engdynamicfield',
            name='input_type',
            field=models.CharField(max_length=50),
        ),
    ]
