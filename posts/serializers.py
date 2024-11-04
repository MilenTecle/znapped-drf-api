from rest_framework import serializers
from .models import Post, Like, Hashtag

class HashtagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Hashtag
    fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    reaction_type = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    video = serializers.FileField(required=False)
    hashtags = HashtagSerializer(many=True, read_only=True)
    hashtag_names = serializers.ListField(write_only=True, required=False)

    def create(self, validated_data):
      hashtag_names = validated_data.pop('hashtag_names', [])
      post = Post.objects.create(**validated_data)
      self._associate_hashtags(post, hashtag_names)
      return post

    def update(self, instance, validated_data):
      hashtag_names = validated_data.pop('hashtag_names', [])
      instance = super().update(instance, validated_data)
      self._associate_hashtags(instance, hashtag_names)
      return instance

    def _associate_hashtags(self, post, hashtag_names):
      hashtags = [
        Hashtag.objects.get_or_create(name=name.strip())[0]
        for name in hashtag_names
      ]
      post.hashtags.set(hashtags)

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def validate_video(self, value):
        if value.size > 100 * 1024 * 1024:
            raise serializers.ValidationError('video size larger than 100MB!')
        return value

    def validate(self, data):
      if data.get ('image') and data.get ('video'):
        raise serializers.ValidationError(
          "You can only upload either an image or a video"
        )
      return data

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    def get_reaction_type(self, obj):
       user = self.context['request'].user
       if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.reaction_type if like else None
       return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'image_filter',
            'like_id', 'reaction_type', 'likes_count',
            'comments_count', 'video','hashtags', 'hashtag_names'
        ]