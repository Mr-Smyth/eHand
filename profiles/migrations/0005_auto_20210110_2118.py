# Generated by Django 3.1.4 on 2021-01-10 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20210102_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='time_balance',
            field=models.DecimalField(choices=[('2 Hours', '2'), ('7 Hours', '7'), ('6 Hours', '6'), ('3 Hours', '3'), ('Not Specified', '0'), ('4 Hours', '4'), ('8 Hours', '8'), ('5 Hours', '5'), ('1 Hour', '1')], decimal_places=2, default='Not Specified', max_digits=4, max_length=40),
        ),
    ]