from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from drf_api.permissions import IsOwnerOrReadOnly
from likes.models import Like
from likes.serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    """
    List likes or create a like if logged in
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer

    def get_queryset(self):
      queryset = Like.objects.all()
      # filter by reaction_type if given in the query
      reaction_type = self.request.query_params.get('reaction_type')
      if reaction_type:
        queryset = queryset.filter(reaction_type=reaction_type)
      return queryset

    def perform_create(self, serializer):
      # Retrieve and validate 'reaction_type' and 'post' from request data
      reaction_type = self.request.data.get('reaction_type')
      post_id = self.request.data.get('post')

      if not reaction_type:
        raise ValidationError({"reaction_type": "No reaction was chosen."})
      if not post_id:
        raise ValidationError({"post": "No post ID was provided."})

      Like.objects.filter(owner=self.request.user, post_id=post_id).delete()

      serializer.save(owner=self.request.user, reaction_type=reaction_type)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def get_queryset(self):
      # Filter likes by reaction_type if provided in the query parameters
      queryset = super().get_queryset()
      reaction_type = self.request.query_params.get('reaction_type')
      if reaction_type:
        queryset = queryset.filter(reaction_type=reaction_type)
      return queryset