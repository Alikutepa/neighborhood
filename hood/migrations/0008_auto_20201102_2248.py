# Generated by Django 3.1.2 on 2020-11-02 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0007_auto_20201102_2223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='description',
            new_name='Location',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]
