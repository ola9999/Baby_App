# Generated by Django 4.0.4 on 2022-05-14 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.FileField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
