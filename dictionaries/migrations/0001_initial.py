# Generated by Django 4.2.6 on 2023-10-10 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DictFirstNameModel',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
