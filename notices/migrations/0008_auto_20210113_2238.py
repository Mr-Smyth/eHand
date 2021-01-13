# Generated by Django 3.1.4 on 2021-01-13 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0007_auto_20210113_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='duration',
            field=models.CharField(choices=[(0, 'Not Specified'), (1, '1 Hour'), (2, '2 Hours'), (3, '3 Hours'), (4, '4 Hours'), (5, '5 Hours'), (6, '6 Hours'), (7, '7 Hours'), (8, '8 Hours')], max_length=1, verbose_name='Duration / Time Payment'),
        ),
    ]
