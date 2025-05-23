# Generated by Django 5.0.4 on 2025-05-23 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('message', models.TextField()),
                ('remind_by', models.CharField(choices=[('email', 'Email'), ('sms', 'SMS')], max_length=10)),
            ],
        ),
    ]
