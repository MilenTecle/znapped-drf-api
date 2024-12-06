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
  """
  View to list all direct messages or create a new message.
  Only authentiated users can access this view.
  """
  permission_classes = [IsOwnerOrReadOnly]
  serializer_class = DirectMessageSerializer

  def get_queryset(self):
    """
    Retrieves messages exchanged with the specified users if a receiver_id is provided.
    Otherwise, retrieves all messages for the logged-in user.
    Filters messages by sender and receiver for the logged-in user.
    """
    user = self.request.user
    receiver_id = self.kwargs.get('pk')

    if receiver_id:
      # Validate that the receiver exists
      other_user = User.objects.filter(id=receiver_id).first()
      if not other_user:
        raise ValidationError(
          {"receiver_id": "No user found with the provided ID."}
        )
      # Retrieve messages exchanged with the specified user
      return DirectMessage.objects.filter(
        models.Q(sender_id=user.id, receiver_id=receiver_id) |
        models.Q(sender=receiver_id, receiver_id=user.id)
      )
    # Retrieve all messages for the logged-in user
    return DirectMessage.objects.filter(
      models.Q(sender=user) | models.Q(receiver=user)
    )


    def perform_create(self, serializer):
      """
      Handles message creation by assigning teh sender as the logged-in user.
      Validates that the specified receiver exists before saving.
      a new message.
      """
      receiver_id = self.request.data.get('receiver')
      if not receiver_id:
        raise ValidationError({"receiver": "This field is required."})

      receiver = User.objects.filter(id=receiver_id).first()
      if not receiver:
        raise ValidationError({"receiver": "User does not exist."})

      # Save the message with sender as the logged-in user
      serializer.save(sender=self.request.user, receiver=receiver, read=False)

class MarkMessageAsRead(APIView):
  """
  Marks selected messages as read for the logged-in message receiver.
  PATCH accepts a list of message IDS in the request data and marks
  the corresponding messages as read and updates message notifications.
  """
  permission_classes = [IsOwnerOrReadOnly]

  def patch(self, request, *args, **kwargs):
    message_ids = request.data.get('message_ids', [])
    if not message_ids:
      return Response({"message": "No message IDs provided"}, status=400)
    DirectMessage.objects.filter(
      id__in=message_ids,
      receiver=request.user
      ).update(read=True)
    notifications_to_update = Notification.objects.filter(
      type="message",
      user=request.user,
      message_id__in=message_ids
    )

    updated_count = notifications_to_update.update(read=True)
    return Response({"Message": "Messages marked as read"})

class DirectMessageDetail(generics.RetrieveUpdateDestroyAPIView):
  """
  View for retrieving, updating or deleting a specific direct message.
  Restricts access to the sender or receiver of the message.
  """
  queryset = DirectMessage.objects.all()
  permission_classes = [IsSenderOrReceiver]
  serializer_class = DirectMessageSerializer

  def get_queryset(self):
      user = self.request.user
      return DirectMessage.objects.filter(
          models.Q(sender=user) | models.Q(receiver=user)
      )