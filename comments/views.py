from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    View for listing all comments or create a comment if logged in.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def perform_create(self, serializer):
        """
        Automatically set the owner of the comment to the
        logged-in user during creation.
        """
        comment = serializer.save(owner=self.request.user)
        comment = Comment.objects.prefetch_related(
            'mentions').get(id=comment.id)

        serializer.instance = comment


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating or deleting a specific comment.
    Ensures only the owner of the comment can update or delete it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
