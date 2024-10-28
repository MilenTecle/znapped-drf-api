from rest_framework import generics, permissions
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
      # filter ty reaction_type if given in the query
      reaction_type = self.request.query_params.get('reaction_type')
      if reaction_type:
        queryset = queryset.filter(reaction_type=reaction_type)
      return queryset

    def perform_create(self, serializer):
      # Ensuer reaction_type is provided in the request data
      reaction_type = self.request.data.get('reaction_type')
      if not reaction_type:
        raise ValidationError({"reaction_type": "No reaction was chosen."})

      # Check for duplicate reaction
      post_id = self.request.data.get('post')
      if Like.objects.filter(
          owner=self.request.user,
          post_id=post_id,
          reaction_type=reaction_type
      ).exists():
          raise ValidationError({"detail": "You have already reacted with this "
           "type on this post"})

      serializer.save(owner=self.request.user, reaction_type=reaction_type)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def get_queryset(self):
      # Get the default queryset from all Like objects
      queryset = super().get_queryset()
      reaction_type = self.request.query_params.get('reaction_type')
      if reaction_type:
        queryset = queryset.filter(reaction_type=reaction_type)
      return queryset