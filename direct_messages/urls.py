from django.urls import path
from direct_messages import views

urlpatterns = [
    path('<int:pk>/', views.DirectMessageList.as_view()),
    path('mark-as-read/', views.MarkMessageAsRead.as_view()),
]