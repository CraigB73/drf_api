from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Profile
from .serializer import ProfileSerializer
from drf_api.permissions import IsOwnerOrReadOnly

class ProfileList(generics.ListAPIView):
    """
    List all profiles
    No create view as profile creation is handled by django (signals)
    """
    #Read abount annotate
    queryset = Profile.objects.annotate(
        post_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    
    filterset_fields = [
        'owner__following__followed__profile'
        
    ]
    ordering_fields = [
        'post_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
        ]
    
class ProfileDetailView(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner
    """
    serializer_class = ProfileSerializer #Will add a form base on serialize
    queryset = Profile.objects.all()
    permission_classes = [IsOwnerOrReadOnly] #need to be and array
    queryset = Profile.objects.annotate(
        post_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')


   
    #imports:
    # from django.http import Http404 
    # from rest_framework.response import Response
    # from rest_framework import status
    # Below is with signal and generic:
    # def get_object(self, pk):
    #     try:
    #         #get profile using primary key
    #         profile = Profile.objects.get(pk=pk)
    #         self.check_object_permissions(self.request, profile)
    #         return profile
    #     except Profile.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk ):
    #     profile= self.get_object(pk)
    #     serializer = ProfileSerializer(
    #         profile, context={'request': request}
    #         )
    #     return Response(serializer.data)

    # def put(self, request, pk):
    #     profile = self.get_object(pk)
    #     serializer = ProfileSerializer(
    #         profile, data=request.data, context={'request': request}
    #         )
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         serializer.errors, status=status.HTTP_400_BAD_REQUEST
    #         )

    # def delete(self, pk):
    #     profile = self.get_object(pk)
    #     profile.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)