# Generated by Django 4.2.5 on 2024-02-12 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='Pending', max_length=20),
        ),
    ]
