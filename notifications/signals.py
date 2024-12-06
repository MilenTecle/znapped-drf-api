from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from comments.models import Comment
from followers.models import Follower
from likes.models import Like
from notifications.models import Notification
from direct_messages.models import DirectMessage

@receiver(post_save, sender=Comment)
def create_mention_notifications(sender, instance, created, **kwargs):
  """
  Creates a notification when a user is mentioned in a comment.
  Ensures the user is not the comment owner and prevents duplicate
  notifications by checking if it exists first.
  """
  if not created:
    return

  for user in instance.mentions.all():
    if user != instance.owner:
      if not Notification.objects.filter(
          user=user,
          sender=instance.owner,
          type="mention",
          post_id=instance.post
      ).exists():
            Notification.objects.create(
                user=user,
                sender=instance.owner,
                type="mention",
                message=f"{instance.owner.username} mentioned you in a comment",
                post_id=instance.post
            )

@receiver(post_save, sender=Follower)
def create_follow_notifications(sender, instance, created, **kwargs):
  """
  Listens for the creation of a new follower instance and
  creates a notification with a custom message.
  """
  if created:
    if instance.owner != instance.followed:
      Notification.objects.create(
        user=instance.followed,
        sender=instance.owner,
        type="follow",
        message=f"{instance.owner.username} started following you.",
        )

@receiver(post_save, sender=Like)
def create_like_notifications(sender, instance, created, **kwargs):
  """
  Creates a notification when a post is liked by a user with a custom message.
  Ensures the notification is not sent to the post owner.
  """
  if created:
    post = instance.post
    post_owner = post.owner

    if instance.owner != post_owner:
      Notification.objects.create(
        user=post_owner,
        sender=instance.owner,
        type="like",
        message=f"{instance.owner.username} liked your post.",
        post_id=post,
        )

@receiver(post_save, sender=DirectMessage)
def create_message_notifications(sender, instance, created, **kwargs):
  """
  Creates a notification when a direct message is sent with a custom message.
  """
  if created:
      Notification.objects.create(
        user=instance.receiver,
        sender=instance.sender,
        type="message",
        message=f"You have a new message from {instance.sender.username}.",
        message_id=instance,
        )
