# Generated by Django 4.1.7 on 2023-09-27 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foli', '0016_alter_member_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='answer1',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='answer2',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='answer3',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='answer4',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='question1',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='question2',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='question3',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='question4',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
    ]