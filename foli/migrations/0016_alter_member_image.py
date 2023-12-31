# Generated by Django 4.1.7 on 2023-09-26 21:48

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('foli', '0015_alter_service_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format=None, keep_meta=True, quality=100, scale=None, size=[385, 300], upload_to='profile'),
        ),
    ]
