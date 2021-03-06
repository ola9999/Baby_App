# Generated by Django 4.0.4 on 2022-05-15 21:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_alter_account_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='geo_entity_pic')),
                ('data', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='birth',
            field=models.DateField(default=datetime.date(2022, 5, 16), null=True, verbose_name='birth'),
        ),
    ]
