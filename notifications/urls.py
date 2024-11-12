from django.urls import path
from likes import views

urlpatterns = [
    path('notifications/', views.NotificationList.as_view()),
    path('notifications/<int:pk>/', views.NotificationUpdate.as_view()),
]