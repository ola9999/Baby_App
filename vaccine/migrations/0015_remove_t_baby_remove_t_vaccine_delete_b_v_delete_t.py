# Generated by Django 4.0.4 on 2022-05-11 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0014_rename_tryy_t_vaccine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='t',
            name='baby',
        ),
        migrations.RemoveField(
            model_name='t',
            name='vaccine',
        ),
        migrations.DeleteModel(
            name='B_V',
        ),
        migrations.DeleteModel(
            name='t',
        ),
    ]
