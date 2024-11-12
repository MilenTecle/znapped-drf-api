from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer

class NotificationList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
      return Notification.objects.filter(user=self.request.user).order_by('-creatad_at')

class NotificationUpdate(generics.UpdateAPIView):
  permission_classes = [IsAuthenticated]
  serializer_class = NotificationSerializer

  def get_queryset(self):
    return Notification.objects.filter(user=self.request.user, read=False)




