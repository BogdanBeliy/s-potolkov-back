# Generated by Django 3.1.2 on 2020-11-15 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_auto_20201115_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newclient',
            old_name='light',
            new_name='dot_light',
        ),
    ]
