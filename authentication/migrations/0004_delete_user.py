# Generated by Django 4.2.6 on 2023-10-30 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_user_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
