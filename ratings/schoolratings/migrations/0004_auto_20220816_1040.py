# Generated by Django 3.1 on 2022-08-16 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolratings', '0003_auto_20220816_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultlog',
            name='grades',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='resultlog',
            name='total_students',
            field=models.TextField(default=1),
        ),
    ]