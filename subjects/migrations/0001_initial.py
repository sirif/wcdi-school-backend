# Generated by Django 4.2.6 on 2023-10-11 04:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dictionaries', '0002_dictsecondnamemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='teacher_set', to='dictionaries.dictfirstnamemodel')),
                ('second_name', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='teacher_set', to='dictionaries.dictsecondnamemodel')),
            ],
        ),
    ]
