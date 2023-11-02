from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    # CONVERSATION_TYPES = (
    #     ('group', 'Group'),
    #     ('one_to_one', 'One-to-One'),
    # )
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)


class Message(models.Model):
    room = models.ForeignKey(
        Chat, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)


# class GroupChat(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     slug = models.SlugField(unique=True)


# class Conversation(models.Model):
#     CONVERSATION_TYPES = (
#         ('group', 'Group'),
#         ('one_to_one', 'One-to-One'),
#     )
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(unique=True)
#     conversation_type = models.CharField(
#         max_length=10, choices=CONVERSATION_TYPES)

# class Message(models.Model):
#     conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
#     user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
#     content = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)
#     is_group_message = models.BooleanField(default=False)

#     class Meta:
#         ordering = ('date_added',)
