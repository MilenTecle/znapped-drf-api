from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from comments.models import Comment
from followers.models import Follower
from likes.models import Like
from .models import Notification

@receiver(post_save, sender=Comment)
def create_mention_notifications(sender, instance, created, **kwargs):
  if created:
    print(f"Signal triggered for comment: {instance.id}")
    for user in instance.mentions.all():
      print(f"Creating notification for: {user}")
      if user != instance.owner:
          try:
            Notification.objects.create(
                user=user,
                sender=instance.owner,
                type="mention",
                message=f"{instance.owner.username} mentioned you in a comment.",
                post_id=instance.post
            )
            print(f"Noticiation created for {user}")
          except Exception as e:
            print(f"Error creating notifications: {e}")

@receiver(post_save, sender=Follower)
def create_follow_notifications(sender, instance, created, **kwargs):
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
