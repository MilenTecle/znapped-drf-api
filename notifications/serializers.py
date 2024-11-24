from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
  user = serializers.ReadOnlyField(source='user.username')
  sender = serializers.ReadOnlyField(source='sender.username')
  sender_profile_id = serializers.ReadOnlyField(source='sender.profile.id')
  post_id = serializers.ReadOnlyField(source='post_id.id')
  direct_message_id = serializers.ReadOnlyField(source='direct_message_id.id')

  class Meta:
    model = Notification
    fields = ['id', 'user', 'sender', 'type', 'message', 'created_at', 'read',
    'post_id', 'direct_message_id', 'sender_profile_id'
  ]