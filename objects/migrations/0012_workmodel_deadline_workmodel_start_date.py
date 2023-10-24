# Generated by Django 4.2.6 on 2023-10-24 05:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0011_alter_estimatemodel_grade_date_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workmodel',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workmodel',
            name='start_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
