# Generated by Django 3.1.4 on 2021-02-11 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0012_auto_20210211_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='package_type',
            field=models.CharField(choices=[('Premium', 'prem'), ('Free', 'free')], default='Free', max_length=40),
        ),
    ]
