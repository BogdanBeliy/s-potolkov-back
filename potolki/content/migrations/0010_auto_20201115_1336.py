# Generated by Django 3.1.2 on 2020-11-15 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_auto_20201115_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsalepotolok',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
