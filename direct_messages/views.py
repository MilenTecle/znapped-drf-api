from django.db import models
from rest_framework import generics
from rest_framework.views import APIView
from drf_api.permissions import IsOwnerOrReadOnly, IsSenderOrReceiver
from django.contrib.auth.models import User
from rest_framework.response import Response
from .models import DirectMessage
from notifications.models import Notification
from .serializers import DirectMessageSerializer
from rest_framework.exceptions import ValidationError

class DirectMessageList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = DirectMessageSerializer

    def get_queryset(self):
      user = self.request.user
      receiver_id = self.kwargs.get('pk')

      if receiver_id:
        other_user = User.objects.filter(id=receiver_id).first()
        if not other_user:
          raise ValidationError({"receiver_id": "No user found with the provided ID."})

        return DirectMessage.objects.filter(
          models.Q(sender_id=user.id, receiver_id=receiver_id) |
          models.Q(sender=receiver_id, receiver_id=user.id)
        )

      return DirectMessage.objects.filter(
          models.Q(sender=user) | models.Q(receiver=user)
        )


    def perform_create(self, serializer):
      receiver_id = self.request.data.get('receiver')
      if not receiver_id:
        raise ValidationError({"receiver": "This field is required."})

      receiver = User.objects.filter(id=receiver_id).first()
      if not receiver:
        raise ValidationError({"receiver": "User does not exist."})
      serializer.save(sender=self.request.user, receiver=receiver, read=False)

class MarkMessageAsRead(APIView):
  permission_classes = [IsOwnerOrReadOnly]

  def patch(self, request, *args, **kwargs):
    message_ids = request.data.get('message_ids', [])
    if not message_ids:
      return Response({"message": "No message IDs provided"}, status=400)
    DirectMessage.objects.filter(id__in=message_ids, receiver=request.user).update(read=True)
    notifications_to_update = Notification.objects.filter(
      type="message",
      user=request.user,
      message_id__in=message_ids
    )

    updated_count = notifications_to_update.update(read=True)
    return Response({"Message": "Messages marked as read"})


class DirectMessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DirectMessage.objects.all()
    permission_classes = [IsSenderOrReceiver]
    serializer_class = DirectMessageSerializer

    def get_queryset(self):
      user = self.request.user
      return DirectMessage.objects.filter(
          models.Q(sender=user) | models.Q(receiver=user)
        )