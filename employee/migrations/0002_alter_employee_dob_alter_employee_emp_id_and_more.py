# Generated by Django 4.2.5 on 2024-01-29 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='ending_date',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='nid',
            field=models.CharField(max_length=500),
        ),
    ]
