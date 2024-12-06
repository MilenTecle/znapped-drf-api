from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from direct_messages.models import DirectMessage

class Notification(models.Model):
  """
  Represents a notification for a user.
  Notifications are triggered by comments, follows, likes, mentions and
  messages.
  """
  NOTIFICATION_TYPES = (
    ('comment', 'Comment'),
    ('follow', 'New Follower'),
    ('like', 'Like'),
    ('mention', 'Mention'),
    ('message', 'Message'),
  )

  user = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="notifications"
  )
  sender = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="sender_notifications"
  )
  type = models.CharField(choices=NOTIFICATION_TYPES, max_length=50)
  message = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  read = models.BooleanField(default=False)
  post_id = models.ForeignKey(
    Post, on_delete=models.CASCADE, null=True, blank=True
  )
  message_id = models.ForeignKey(
    DirectMessage, on_delete=models.CASCADE, null=True, blank=True
  )

  class Meta:
      ordering = ['-created_at']
      unique_together = ['user', 'sender', 'type', 'post_id', 'message_id']

  def __str__(self):
      return f'Notification: {self.type} from {self.sender} to {self.user}'




