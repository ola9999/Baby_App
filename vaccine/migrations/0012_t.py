# Generated by Django 4.0.4 on 2022-05-11 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_account_birth'),
        ('vaccine', '0011_alter_b_v_dead_line'),
    ]

    operations = [
        migrations.CreateModel(
            name='t',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taken', models.BooleanField(default=False)),
                ('dead_line', models.DateField(default=None, editable=False, null=True, verbose_name='date to take')),
                ('baby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
                ('tryy', models.ManyToManyField(to='vaccine.all_vaccines')),
            ],
        ),
    ]
