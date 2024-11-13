from rest_framework import generics
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Notification
from .serializers import NotificationSerializer

class NotificationList(generics.ListAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = NotificationSerializer

    def get_queryset(self):
      if self.request.user.is_authenticated:
        return Notification.objects.filter(user=self.request.user).order_by('-created_at')
      return Notification.objects

class NotificationUpdate(generics.UpdateAPIView):
  permission_classes = [IsOwnerOrReadOnly]
  serializer_class = NotificationSerializer

  def get_queryset(self):
    return Notification.objects.filter(user=self.request.user, read=False)




