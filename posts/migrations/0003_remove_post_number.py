# Generated by Django 4.0.6 on 2022-08-30 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='number',
        ),
    ]
