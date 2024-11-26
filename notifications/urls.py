from django.urls import path
from notifications import views

urlpatterns = [
    path('notifications/', views.NotificationList.as_view()),
    path('notifications/<int:pk>/', views.NotificationUpdate.as_view()),
    path('mark-as-read/', views.MarkAsRead.as_view()),
]