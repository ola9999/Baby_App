# Generated by Django 4.0.4 on 2022-05-11 22:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_account_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='birth',
            field=models.DateField(default=datetime.date(2022, 5, 12), null=True, verbose_name='birth'),
        ),
    ]
