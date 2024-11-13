from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
  user = serializers.ReadOnlyField(source='user.username')
  sender = serializers.ReadOnlyField(source='sender.username')

  class Meta:
    model = Notification
    fields = ['id', 'user', 'sender', 'type', 'message', 'created_at', 'read']