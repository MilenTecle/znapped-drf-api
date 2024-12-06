from django.db import models
from django.contrib.auth.models import User

class Hashtag(models.Model):
  """
  Hashtags used in posts.
  Ensures that hashtags are unique and can be associated with multiple posts.
  """
  name = models.CharField(max_length=50, unique=True)

  def __str__(self):
    return self.name

class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    Includes associated hashtags for categorization.
    """
    image_filter_choices = [
    ('_1977', '1977'), ('brannan', 'Brannan'),
    ('earlybird', 'Earlybird'), ('hudson', 'Hudson'),
    ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'),
    ('kelvin', 'Kelvin'), ('normal', 'Normal'),
    ('nashville', 'Nashville'), ('rise', 'Rise'),
    ('toaster', 'Toaster'), ('valencia', 'Valencia'),
    ('walden', 'Walden'), ('xpro2', 'X-pro II')
]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_ftw1xc', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )
    video = models.FileField(
      upload_to='videos/',
      blank=True,
      null=True,
    )
    hashtags = models.ManyToManyField(
      Hashtag, related_name="posts", blank=True
    )
    mentions = models.ManyToManyField(
      User, related_name="mentions_posts", blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
