# Generated by Django 3.1.2 on 2020-10-31 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20201031_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='imgUrl',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
