# Generated by Django 4.0.4 on 2022-05-12 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_alter_account_arrangement_among_siblings_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='address',
            field=models.CharField(default='default', max_length=250),
        ),
        migrations.AlterField(
            model_name='account',
            name='pragnancyduration',
            field=models.CharField(default='9', max_length=2),
        ),
    ]
