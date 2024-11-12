from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from comments.models import Comment
from followers.models import Follower
from .models import Notification

@receiver(post_save, sender=Comment)
def create_mention_notifications(sender, instance, created, **kwargs):
  if created:
    for user in instance.mention.all():
      Notification.objects.create(
        user=user,
        sender=instance.owner,
        type="mention",
        message=f"{instance.owner.username} mentioned you in a comment.",
        )

@receiver(post_save, sender=Follower)
def create_follow_notifications(sender, instance, created, **kwargs):
  if created:
      Notification.objects.create(
        user=instance.followed,
        sender=instance.owner,
        type="follow",
        message=f"{instance.owner.username} started following you.",
        )

@receiver(post_save, sender=Like)
def create_like_notifications(sender, instance, created, **kwargs):
  if created:
    post_owner = instance.post.owner

    if instance.owner != post.owner:
      Notification.objects.create(
        user=post.owner,
        sender=instance.owner,
        type="like",
        message=f"{instance.owner.username} liked your post.",
        )
