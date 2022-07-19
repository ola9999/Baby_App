# Generated by Django 4.0.4 on 2022-07-19 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_tips_title_alter_tips_tip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='food_name',
            field=models.CharField(default='default food', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='feed',
            name='food_type',
            field=models.CharField(choices=[('رضاعة طبيعية', 'رضاعة طبيعية'), ('حليب صناعي', 'حليب صناعي'), ('فواكه', 'فواكه'), ('خضار', 'خضار'), ('نشويات', 'نشويات'), ('دسم', 'دسم'), ('ماء', 'ماء')], default='default type', max_length=25, null=True),
        ),
    ]
