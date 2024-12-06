from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth.models import User
from drf_api.permissions import IsOwnerOrReadOnly, IsNotificationOwner
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer


class NotificationList(generics.ListAPIView):
    """
    List all notifications for the logged-in user.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = NotificationSerializer

    """
    Retrives notifications for the authenticated user,
    ordered by the most recent.
    """

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Notification.objects.filter(
                user=self.request.user
            ).order_by('-created_at')
        return Notification.objects.none()


class NotificationUpdate(generics.RetrieveUpdateDestroyAPIView):
    """
    Allows the logged-in user to delete a notification.
    """
    permission_classes = [IsNotificationOwner]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)


class MarkAsRead(APIView):
    """
    Mark all unread notifications as read for the logged-in user.
    """
    permission_classes = [IsOwnerOrReadOnly]

    def patch(self, request, *args, **kwargs):
        notifications = Notification.objects.filter(
            user=request.user, read=False)
        notifications.update(read=True)
        return Response({"Message": "Notifications marked as read"})
