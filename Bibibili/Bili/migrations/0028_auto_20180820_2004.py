# Generated by Django 2.0.3 on 2018-08-20 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bili', '0027_auto_20180819_1624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='subscribe_tags',
            new_name='tags',
        ),
    ]