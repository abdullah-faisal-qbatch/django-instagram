# Generated by Django 4.2.6 on 2023-10-27 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_managers_user_date_joined_user_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='john'),
            preserve_default=False,
        ),
    ]
