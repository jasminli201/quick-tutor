# Generated by Django 3.0.3 on 2020-04-11 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TutorSignup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(default='', max_length=12)),
                ('classes', models.TextField(default='', max_length=120)),
                ('subjects', models.CharField(choices=[('science', 'science'), ('math', 'math'), ('english', 'english')], default='', max_length=120)),
                ('pay', models.CharField(default='', max_length=12)),
                ('payment_method', models.CharField(choices=[('venmo', 'venmo'), ('cash', 'cash'), ('paypal', 'paypal')], default='', max_length=120)),
                ('longitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('status', models.BooleanField(default=False)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('accept', 'Accept'), ('deny', 'Deny'), ('No choice', 'No choice')], default='No choice', max_length=32)),
                ('time', models.DateTimeField(verbose_name='time sent')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to=settings.AUTH_USER_MODEL)),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutors', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
