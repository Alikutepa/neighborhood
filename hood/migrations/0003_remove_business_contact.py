# Generated by Django 3.1.2 on 2020-11-02 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0002_auto_20201101_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='contact',
        ),
    ]
