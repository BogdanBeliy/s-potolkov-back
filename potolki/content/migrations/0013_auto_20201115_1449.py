# Generated by Django 3.1.2 on 2020-11-15 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_newsalepotolok_type_sale'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newclient',
            old_name='chois',
            new_name='potolok',
        ),
    ]
