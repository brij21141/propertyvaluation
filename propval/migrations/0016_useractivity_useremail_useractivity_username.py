# Generated by Django 5.1 on 2024-11-11 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propval', '0015_alter_userdetails_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='useractivity',
            name='useremail',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='useractivity',
            name='username',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
