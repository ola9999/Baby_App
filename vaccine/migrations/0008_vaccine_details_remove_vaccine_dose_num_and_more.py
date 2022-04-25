# Generated by Django 4.0.4 on 2022-04-24 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_account_birth'),
        ('vaccine', '0007_remove_vaccine_baby_vaccine_baby'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='name')),
                ('dose_num', models.PositiveSmallIntegerField(default=1)),
                ('static_duration', models.PositiveSmallIntegerField(default=1, verbose_name='static duration in monthes')),
            ],
        ),
        migrations.RemoveField(
            model_name='vaccine',
            name='dose_num',
        ),
        migrations.RemoveField(
            model_name='vaccine',
            name='name',
        ),
        migrations.RemoveField(
            model_name='vaccine',
            name='static_duration',
        ),
        migrations.RemoveField(
            model_name='vaccine',
            name='baby',
        ),
        migrations.AddField(
            model_name='vaccine',
            name='baby',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='account.account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vaccine',
            name='vaccine',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='vaccine.vaccine_details'),
            preserve_default=False,
        ),
    ]
