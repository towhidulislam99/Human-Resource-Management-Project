# Generated by Django 4.2.5 on 2024-02-12 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_alter_attendance_attendence_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attendence_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
