from rest_framework import permissions

"""
The permission class used for the other views.
"""


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


"""
A custom permission class for the DirectMessageDetail
to allow sender or receiver to delete a direct message.
"""


class IsSenderOrReceiver(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.sender == request.user or obj.receiver == request.user


"""
A custom permission class for NotificationUpdste
to allow user to delete a notification.
"""


class IsNotificationOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
