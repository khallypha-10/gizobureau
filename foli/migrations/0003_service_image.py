# Generated by Django 4.2.4 on 2023-08-22 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foli', '0002_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(default='static\\images\\logo-2.png', upload_to='service'),
            preserve_default=False,
        ),
    ]
