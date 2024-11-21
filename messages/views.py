from rest_framework import generics
from rest_framework.views import APIView
from drf_api.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from rest_framework.response import Response
from .models import DirectMessage
from .serializers import DirectMessagSerializer
from rest_framework.exceptions import ValidationError

class DirectMessageList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = DirectMessageSerializer

    def get_queryset(self):
      user = self.request.user
      other_users = self.request.query_params.get('user_id')
      if not other_users:
        return DirectMessage.objects.none()
      return DirectMessage.objects.filter(
        (models.Q(sender=user) & models.Q(receiver_id=other_users)) |
        (models.Q(sender_id=other_users) & moedels.Q(receiver=user))
      )

    def perform_create(self, serializer):
      receiver_id = self.request.data.get('receiver_id')
      if not receiver_id:
        raise ValidationError({"receiver_id": "This field is required."})
      receiver = User.objects.filter(id=receiver_id).first()
      if not receiver:
        raise ValidationError({"receiver_id": "User does not exist."})
      serializer.save(sender=self.request.user, receiver=receiver)

class MarkMessageAsRead(APIView):
  permission_classes = [IsOwnerOrReadOnly]

  def patch(self, request, *args, **kwargs):
    message_ids = request.data.get('message_ids', [])
    if not message_ids:
      return Response({"message": "No message IDs provided"}, status=400)
    DirectMessage.objects.filter(id__in=message_ids, receiver=request.user).update(read=True)
    return Response({"Message": "Messages marked as read"})

