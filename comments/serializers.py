from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment
from django.contrib.auth.models import User


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    Adds three extra fields when returning a list of Comment instances.
    Includes additional fields for handling mentions.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    mentions = serializers.StringRelatedField(many=True, read_only=True)
    mention_usernames = serializers.ListField(write_only=True, required=False)

    def get_is_owner(self, obj):
        """
        Check if the requesting user is the owner of the comment.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        """
        Return a readable created_at timestamp using naturaltime
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    def create(self, validated_data):
        """
        Create a comment and associate mentions based
        on provided usernames. Extract mentioned usernames,
        find users my usernames, create the comment and associate
        the mentions with the comment.
        """
        mention_usernames = validated_data.pop('mention_usernames', [])
        mentioned_users = User.objects.filter(username__in=mention_usernames)

        comment = super().create(validated_data)

        if mentioned_users.exists():
            comment.mentions.set(mentioned_users)

        return comment

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'post', 'created_at', 'updated_at', 'content', 'mention_usernames',
            'mentions'
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """
    post = serializers.ReadOnlyField(source='post.id')
