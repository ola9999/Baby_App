# Generated by Django 4.0.4 on 2022-05-19 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_album_baby'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lalluby',
            name='song_name',
        ),
    ]
