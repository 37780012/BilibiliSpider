# Generated by Django 2.0.3 on 2018-08-21 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bili', '0029_auto_20180820_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(default='保密', help_text='性别', max_length=4, verbose_name='性别'),
        ),
    ]