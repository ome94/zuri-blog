# Generated by Django 3.2 on 2021-04-27 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Reader',
        ),
    ]
