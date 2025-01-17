# Generated by Django 5.1 on 2025-01-02 06:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propval', '0024_impdoc_pdf_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='EngFormOptionValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opt_value', models.CharField(blank=True, max_length=40, null=True)),
                ('eng_dynamic_field', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='options', to='propval.engdynamicfield')),
            ],
        ),
    ]
