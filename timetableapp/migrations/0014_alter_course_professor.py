# Generated by Django 5.0.3 on 2024-04-28 23:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetableapp', '0013_rename_professer_course_professor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetableapp.professor'),
        ),
    ]
