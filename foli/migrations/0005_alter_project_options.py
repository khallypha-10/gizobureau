# Generated by Django 4.2.4 on 2023-08-23 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foli', '0004_service_icon'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-date']},
        ),
    ]