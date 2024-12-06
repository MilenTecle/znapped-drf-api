from django.urls import path
from notifications import views

urlpatterns = [
    path("", views.NotificationList.as_view()),
    path("<int:pk>/", views.NotificationUpdate.as_view()),
    path("mark-as-read/", views.MarkAsRead.as_view()),
]
