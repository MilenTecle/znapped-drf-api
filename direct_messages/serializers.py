from rest_framework import serializers
from .models import DirectMessage

class DirectMessageSerializer(serializers.ModelSerializer):
  sender_name = serializers.ReadOnlyField(source='sender.username')
  receiver_name = serializers.ReadOnlyField(source='receiver.username')

  class Meta:
    model = DirectMessage
    fields = ['id', 'sender', 'receiver', 'sender_name', 'receiver_name',
    'content', 'created_at', 'read'
    ]
    read_only_fields = ['sender', 'receiver']