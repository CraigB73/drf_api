from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from .models import Profile
from .serializer import ProfileSerializer
from rest_framework import status
from drf_api.permissions import IsOwnerOrReadOnly

class ProfileList(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True, context={'request': request})
        return Response(serializer.data)
    

class ProfileDetailView(APIView):
    serializer_class = ProfileSerializer #Will add a form base on serialize
    permission_classes = [IsOwnerOrReadOnly] #need to be and array
    def get_object(self, pk):
        try:
            #get profile using primary key
            profile = Profile.objects.get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile 
        except Profile.DoesNotExist:
            raise Http404
    
    def get(self, request, pk ):
        profile= self.get_object(pk)
        serializer = ProfileSerializer(profile, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, pk):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)