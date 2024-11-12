from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
  NOTIFICATION_TYPES = (
    ('comment', 'Comment'),
    ('follow', 'New Follower'),
    ('like', 'Like'),
    ('mention', 'Mention')
  )

  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
  sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender_notifications")
  type = models.CharField(choices=NOTIFICATION_TYPES, max_length=50)
  message = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  read = models.BooleanField(default=False)

  class Meta:
      ordering = ['-created_at']
      unique_together = ['user', 'sender', 'type']

  def __str__(self):
      return f'Notification: {self.type} from {self.sender} to {self.user}'




