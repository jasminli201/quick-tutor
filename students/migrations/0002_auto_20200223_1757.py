# Generated by Django 3.0.3 on 2020-02-23 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsignup',
            name='classes',
            field=models.TextField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='studentsignup',
            name='phone_number',
            field=models.CharField(default='', max_length=12),
        ),
    ]
