# Generated by Django 3.0.2 on 2020-01-17 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0009_auto_20200118_0100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='user',
        ),
    ]
