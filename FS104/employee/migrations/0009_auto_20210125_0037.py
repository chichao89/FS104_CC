# Generated by Django 3.1.4 on 2021-01-24 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_auto_20210125_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='dept_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]