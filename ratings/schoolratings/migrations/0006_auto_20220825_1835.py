# Generated by Django 3.1 on 2022-08-25 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolratings', '0005_resultlog_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resultlog',
            old_name='city',
            new_name='address',
        ),
    ]