# Generated by Django 4.0.4 on 2022-05-15 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_alter_account_birth'),
        ('app', '0012_remove_album_baby'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='baby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.account'),
        ),
    ]
