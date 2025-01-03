from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    """
    Comment model, each comments is linked to a user (owner)
    and a post. Mentions for tagging users within a comment.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    mentions = models.ManyToManyField(
        User, related_name="mention_comments", blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
