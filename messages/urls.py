from django.urls import path
from messages import views

urlpatterns = [
    path('', views.DirectMessageList.as_view()),
    path('mark-as-read/', views.MarkMessageAsRead.as_view()),
]