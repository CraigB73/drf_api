from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializer import LikeSerializer
# Create your views here.

class LikeList(generics.ListCreateAPIView):
    """
    List likes or create a like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
  
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
      
    