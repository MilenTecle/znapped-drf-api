from django.db import models
from django.contrib.auth.models import User


class DirectMessage(models.Model):
    """
    Message model for direct messages between users.
    Each message is linked to a sender and a receiver.
    Includes content, timestamps and a read status.
    """
    sender = models.ForeignKey(
        User, related_name='sent_messages', on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        User, related_name='received_messages', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
