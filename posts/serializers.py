from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Hashtag
from likes.models import Like


class HashtagSerializer(serializers.ModelSerializer):
    """
    Serializer for Hashtag model.
    """
    class Meta:
        model = Hashtag
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model.
    Displays related data.
    Creating or updating posts with associated hashtags.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    reaction_type = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    hashtags = HashtagSerializer(many=True, read_only=True)
    hashtag_names = serializers.ListField(write_only=True, required=False)
    mentions = UserSerializer(many=True, read_only=True)
    mention_usernames = serializers.ListField(write_only=True, required=False)

    def create(self, validated_data):
        """
        Handles post creation and associated hashtags.
        """
        hashtag_names = validated_data.pop('hashtag_names', [])
        mention_usernames = validated_data.pop('mention_usernames', [])
        post = Post.objects.create(**validated_data)
        self._associate_hashtags(post, hashtag_names)
        self._associate_mentions(post, mention_usernames)
        return post

    def update(self, instance, validated_data):
        """
        Updates a post and updates associated hashtags.
        """
        hashtag_names = validated_data.pop('hashtag_names', [])
        mention_usernames = validated_data.pop('mention_usernames', [])
        instance = super().update(instance, validated_data)
        self._associate_hashtags(instance, hashtag_names)
        self._associate_mentions(instance, mention_usernames)
        return instance

    def _associate_hashtags(self, post, hashtag_names):
        """
        Associate hashtags with a post. Creates new hashtags if the don't
        exist.
        """
        hashtags = [
            Hashtag.objects.get_or_create(name=name.strip())[0]
            for name in hashtag_names
        ]
        post.hashtags.set(hashtags)

    def _associate_mentions(self, post, mention_usernames):
        users = User.objects.filter(username__in=mention_usernames)
        post.mentions.set(users)

    def validate_image(self, value):
        """
        Validation for uploading images when creating a post.
        """
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

    def get_is_owner(self, obj):
        """
        Checks if the logged-in user is the owner of the post.
        """
        request = self.context['request']
        if not request:
            return False
        return request.user == obj.owner

    def get_like_id(self, obj):
        """
        Retrieves the ID of the like associated with the logged-in user for the
        current post.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    def get_reaction_type(self, obj):
        """
        Retrieves the ID of the reaction type the logged-in user has
        given to the post.
        """
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
            'comments_count', 'video', 'hashtags', 'hashtag_names',
            'mention_usernames', 'mentions'
        ]
