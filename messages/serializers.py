from rest_framework import serializers
from .models import DirectMessage

class DirectMessagSerializer(serializers.ModelSerializer):
  sender = serializers.ReadOnlyField(source='sender.username')
  receiver = serializers.ReadOnlyField(source='receiver.username')

  class Meta:
    model = DirectMessage
    fields = ['id', 'sender', 'receiver', 'content', 'created_at', 'read']