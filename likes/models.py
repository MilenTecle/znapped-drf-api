from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Reaction(models.TextChoices):
  HEART = 'heart', 'Heart'
  THUMBS_UP = 'thumps_up', 'Thumps Up'
  LAUGH = 'laugh', 'Laugh'
  SAD = 'sad', 'Sad'
  ANGRY = 'angry', 'Angry'

class Like(models.Model):
    """
    Like model, related to 'owner' and 'post'.
    'owner' is a User instance and 'post' is a Post instance.
    'unique_together' makes sure a user can't like the same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    reaction_type = models.CharField(
        max_length=10, choices=Reaction.choices, default=Reaction.HEART
    )

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post', 'reaction_type']

    def __str__(self):
        return f'{self.owner} {self.post} {self.reaction_type}'


