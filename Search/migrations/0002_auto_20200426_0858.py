# Generated by Django 2.0.2 on 2020-04-26 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Search', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='PostTitle',
            new_name='title',
        ),
    ]
