# Generated by Django 3.1.2 on 2020-10-31 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20201031_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='gallery/')),
                ('title', models.TextField(default='Изготовление и монтаж натяжных потолков в Минске и минской области | s-potolkov | s potolkov | spotolok')),
            ],
        ),
        migrations.CreateModel(
            name='NewClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('area', models.IntegerField(default='')),
                ('light', models.IntegerField(default='')),
                ('chois', models.CharField(max_length=300)),
            ],
        ),
    ]
