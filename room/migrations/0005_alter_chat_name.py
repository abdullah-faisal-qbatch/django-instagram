# Generated by Django 4.2.6 on 2023-11-06 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0004_chat_created_at_chat_group_chat_chat_user_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='name',
            field=models.CharField(default='null', max_length=255),
        ),
    ]
