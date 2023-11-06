# Generated by Django 4.2.6 on 2023-11-06 08:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0006_remove_chat_name_remove_chat_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='chat',
            name='slug',
            field=models.SlugField(unique=True),
            preserve_default=False,
        ),
    ]
