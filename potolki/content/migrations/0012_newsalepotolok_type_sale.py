# Generated by Django 3.1.2 on 2020-11-15 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_auto_20201115_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsalepotolok',
            name='type_sale',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
