# Generated by Django 4.0.4 on 2022-04-23 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0002_alter_vaccine_dead_line'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccine',
            name='static_duration',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='static duration in monthes'),
        ),
    ]
