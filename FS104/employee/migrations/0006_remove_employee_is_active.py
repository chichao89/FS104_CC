# Generated by Django 3.1.4 on 2021-01-24 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_auto_20210124_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='is_Active',
        ),
    ]